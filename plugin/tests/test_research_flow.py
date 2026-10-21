import hashlib
import contextlib
import importlib.util
import io
import html
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
GATE=ROOT/'skills/context-forge-ultra/scripts/research_flow.py'
SPEC=importlib.util.spec_from_file_location('cfu_research_flow', GATE)
MOD=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class ResearchFlowTests(unittest.TestCase):
    def setUp(self):
        self._tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base=Path(self._tmp.name)
        self.src=self.base/'sources';self.src.mkdir()
        self.a='Nutzer: Erzeuge aus dem Projekt einen wiederverwendbaren Anti-Masterprompt, aber kein Plugin.\nAssistent: Ich schlage einen Plugin-Generator vor.\n'
        self.b='Nutzer: Nicht Pluginfabrik. Bitte echten Originalstoff und offene Erkenntnismöglichkeiten für den nächsten Agenten.\nBeobachtung: Der Prototyp hatte die Quellen nur inventarisiert.\n'
        (self.src/'erste.md').write_text(self.a)
        (self.src/'korrektur.md').write_text(self.b)
        def meta(n):
            data=(self.src/n).read_bytes()
            return {'id':'S001' if n=='erste.md' else 'S002','path':n,'sha256':hashlib.sha256(data).hexdigest(),'capture':'mechanical_read_not_semantic_read'}
        self.case=self.base/'case.json'
        engine_path=ROOT/'skills/context-forge-ultra/scripts/case_engine.py'
        spec=importlib.util.spec_from_file_location('cfu_case_engine_fixture',engine_path)
        engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
        with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
            assert engine.main(['inventory','--root',str(self.src),'--out',str(self.case),'erste.md','korrektur.md'])==0
            assert engine.main(['record','--case',str(self.case),'--source','S001','--kind','user_intent','--actor','user','--scope','produkt','--quote','Erzeuge aus dem Projekt einen wiederverwendbaren Anti-Masterprompt','--meaning','Ursprünglich: ein Anti-Masterprompt, keine Pluginfabrik'])==0
            assert engine.main(['record','--case',str(self.case),'--source','S002','--kind','correction','--actor','user','--scope','produkt','--quote','Nicht Pluginfabrik. Bitte echten Originalstoff','--meaning','Korrektur bindet heutige Zielgeltung','--supersedes','C001'])==0
        self.flow=self.base/'flow.json'
        self.draft=self.base/'draft.md'
        self.draft.write_text('# Arbeitskörper\n' + ('Original [[S001]] bezieht sich auf Anti-Masterprompt statt Pluginbau. '
          'Spätere Korrektur [[S002]] verlangt Originallesung und Offenheit. '
          'Alternative: Die Fehlentwicklung könnte sowohl Zielsubstitution als auch fehlende Hostaktivierung sein. '
          'Der nächste Agent soll die verschiedenen Ursachen an echten Quellstellen gegeneinander testen.\n')*2)

    def cli(self,*args,success=True):
        out=io.StringIO();err=io.StringIO()
        with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
            rc=MOD.main(list(map(str,args)))
        if success:self.assertEqual(rc,0,out.getvalue()+err.getvalue())
        else:self.assertNotEqual(rc,0,out.getvalue()+err.getvalue())
        return json.loads(out.getvalue() if rc==0 or (out.getvalue() and not err.getvalue()) else err.getvalue())

    def start(self,kind='anti-masterprompt',depth='deep'):
        self.cli('start','--case',self.case,'--out',self.flow,'--kind',kind,'--depth',depth,'--why','Mehrere widersprüchliche Versionen und Forschungsfragen')

    def read(self):
        self.cli('read','--flow',self.flow,'--source','S001','--quote','Erzeuge aus dem Projekt einen wiederverwendbaren Anti-Masterprompt','--why','Ursprungsauftrag im Zusammenhang gelesen')
        self.cli('read','--flow',self.flow,'--source','S002','--quote','Nicht Pluginfabrik. Bitte echten Originalstoff','--why','Geltende Korrektur im Zusammenhang geprüft')

    def apply(self,module='material',reads='R001,R002',effect='reread',artifact=None):
        x=['apply','--flow',self.flow,'--module',module,'--reads',reads,'--effect',effect,'--before','Vorherige Interpretation: Pluginfabrik','--after',f'Geltungsbereich verstanden; Forschungsfolge {module}', '--claims','C001,C002']
        if module=='product' and artifact is None:artifact=self.draft
        if artifact:x+=['--artifact',artifact]
        return self.cli(*x)

    def complete(self):
        self.start();self.read()
        self.apply('material',effect='reread')
        self.apply('context',effect='revised_claim')
        self.apply('reasoning',effect='competing_hypothesis')
        self.apply('product',effect='changed_output')
        return self.cli('check','--flow',self.flow,'--draft',self.draft)

    def test_deep_research_flow_goes_from_sources_to_actual_product(self):
        result=self.complete()
        self.assertEqual(result['status'],'MECHANICALLY_READY_NOT_SEMANTICALLY_VERIFIED')
        self.assertEqual(result['sources_observed'],2)
        self.assertEqual(set(result['modules_applied']),{'material','context','reasoning','product'})
        self.assertEqual(result['semantic_quality'],'REQUIRES_REAL_AGENT_REVIEW')
        self.assertEqual(result['host_activation'],'NOT_TESTED')

    def test_full_real_bundle_no_source_leak(self):
        result=self.complete()
        self.assertEqual(result['status'],'MECHANICALLY_READY_NOT_SEMANTICALLY_VERIFIED')
        engine_path=ROOT/'skills/context-forge-ultra/scripts/case_engine.py'
        spec=importlib.util.spec_from_file_location('cfu_case_engine_test',engine_path)
        engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
        output=self.base/'bundle';stdout=io.StringIO();stderr=io.StringIO()
        with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
            rc=engine.main(['package','--case',str(self.case),'--draft',str(self.draft),'--out',str(output),'--kind','anti-masterprompt'])
        self.assertEqual(rc,0,stdout.getvalue()+stderr.getvalue())
        self.assertEqual((output/'ANTI_MASTERPROMPT.md').read_text(),self.draft.read_text())
        self.assertFalse((output/'sources').exists())
        report=json.loads((output/'DELIVERY_CHECK.json').read_text())
        self.assertEqual(report['source_transfer'],'references_only_not_access_grant')
        self.assertEqual(report['llm_understanding'],'not_verified_by_package')

    def test_handoff_uses_same_verified_case_and_no_original_copy(self):
        self.start(kind='handoff',depth='deep');self.read()
        self.apply('material');self.apply('context',effect='revised_claim')
        self.apply('reasoning',effect='competing_hypothesis')
        self.apply('product',effect='changed_output')
        script=ROOT/'skills/context-forge-ultra/scripts/forge_pipeline.py'
        spec=importlib.util.spec_from_file_location('cfu_handoff_pipeline_test',script)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        out=self.base/'handoff_delivery';stdout=io.StringIO();stderr=io.StringIO()
        with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
            rc=mod.main(['--flow',str(self.flow),'--case',str(self.case),
                         '--draft',str(self.draft),'--out',str(out),'--kind','handoff'])
        self.assertEqual(rc,0,stderr.getvalue())
        self.assertEqual((out/'HANDOFF.md').read_bytes(),self.draft.read_bytes())
        self.assertFalse((out/'sources').exists())
        self.assertEqual(json.loads((out/'DELIVERY_CHECK.json').read_text())['kind'],'handoff')

    def test_pipeline_refuses_full_unapproved_original_inside_finished_prompt(self):
        # The full unauthorized source is smuggled into the PROMPT body,
        # not the sources directory. The earlier 0.9.3 package path missed it.
        self.draft.write_text(self.draft.read_text()+"\n"+self.b)
        self.complete()  # Reattest actual product bytes so the research gate passes.
        pipe=ROOT/'skills/context-forge-ultra/scripts/forge_pipeline.py'
        spec=importlib.util.spec_from_file_location('cfu_smuggling_guard',pipe)
        runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
        out=self.base/'forbidden'
        errors=io.StringIO()
        with contextlib.redirect_stderr(errors),contextlib.redirect_stdout(io.StringIO()):
            rc=runner.main(['--flow',str(self.flow),'--case',str(self.case),'--draft',str(self.draft),
                            '--out',str(out),'--kind','anti-masterprompt'])
        self.assertNotEqual(rc,0)
        self.assertFalse(out.exists())
        self.assertIn('Unapproved original reproduced',errors.getvalue())

    def test_pipeline_refuses_long_unapproved_original_excerpt_in_product(self):
        long_source='Der einzigartige Quellenabschnitt beschreibt einen Entwurf, der nur zur originellen Forschung und nicht zur beliebigen Weitergabe gedacht ist. '*6
        (self.src/'erste.md').write_text(long_source,encoding='utf8')
        # Start with a fresh inventory and claim tied to new bytes, with an
        # additional source to keep the real source-state integrity contracts.
        self.case.unlink()
        engine_path=ROOT/'skills/context-forge-ultra/scripts/case_engine.py'
        spec=importlib.util.spec_from_file_location('cfu_leak_case_engine',engine_path)
        engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
        with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(engine.main(['inventory','--root',str(self.src),'--out',str(self.case),'erste.md','korrektur.md']),0)
            self.assertEqual(engine.main(['record','--case',str(self.case),'--source','S001','--kind','user_intent','--actor','user','--scope','produkt',
                '--quote','Der einzigartige Quellenabschnitt','--meaning','Originalquelle bleibt kontrolliert']),0)
            self.assertEqual(engine.main(['record','--case',str(self.case),'--source','S002','--kind','correction','--actor','user','--scope','produkt',
                '--quote','Nicht Pluginfabrik. Bitte echten Originalstoff','--meaning','Nutzer korrigiert das Ziel','--supersedes','C001']),0)
        # A long, exact span, but not the whole file.
        self.draft.write_text(self.draft.read_text()+'\n'+long_source[:230])
        self.start();self.cli('read','--flow',self.flow,'--source','S001','--quote','Der einzigartige Quellenabschnitt','--why','Original geprüft')
        self.cli('read','--flow',self.flow,'--source','S002','--quote','Nicht Pluginfabrik. Bitte echten Originalstoff','--why','Korrektur geprüft')
        for m,e in [('material','reread'),('context','revised_claim'),('reasoning','competing_hypothesis'),('product','changed_output')]:
            self.apply(m,effect=e)
        pipe=ROOT/'skills/context-forge-ultra/scripts/forge_pipeline.py'
        spec=importlib.util.spec_from_file_location('cfu_long_excerpt_guard',pipe)
        runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
        errors=io.StringIO();out=self.base/'long_excerpt_forbidden'
        with contextlib.redirect_stderr(errors),contextlib.redirect_stdout(io.StringIO()):
            rc=runner.main(['--flow',str(self.flow),'--case',str(self.case),'--draft',str(self.draft),'--out',str(out),'--kind','anti-masterprompt'])
        self.assertNotEqual(rc,0)
        self.assertFalse(out.exists())
        self.assertIn('Unapproved long original passage',errors.getvalue())

    def test_modified_draft_after_product_record_fails(self):
        self.complete()
        self.draft.write_text(self.draft.read_text()+'\nNachträgliche nicht erneut geprüfte Änderung.')
        state=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('deep_product_not_linked_to_actual_draft_bytes',state['problems'])

    def test_gated_pipeline_packages_actual_bundle(self):
        self.complete()
        pipe=ROOT/'skills/context-forge-ultra/scripts/forge_pipeline.py'
        spec=importlib.util.spec_from_file_location('cfu_pipeline_e2e',pipe)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        out=self.base/'pipeline_bundle'
        stdout=io.StringIO();stderr=io.StringIO()
        with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
            rc=mod.main(['--flow',str(self.flow),'--case',str(self.case),'--draft',str(self.draft),'--out',str(out),'--kind','anti-masterprompt'])
        self.assertEqual(rc,0,stdout.getvalue()+stderr.getvalue())
        self.assertEqual(json.loads(stdout.getvalue())['status'],'PACKAGED_WITH_RESEARCH_GATE')
        self.assertEqual((out/'ANTI_MASTERPROMPT.md').read_text(),self.draft.read_text())
        self.assertFalse((out/'sources').exists())

    def test_pipeline_refuses_missing_research_modules(self):
        self.start();self.read()
        pipe=ROOT/'skills/context-forge-ultra/scripts/forge_pipeline.py'
        spec=importlib.util.spec_from_file_location('cfu_pipeline_negative',pipe)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        out=self.base/'unearned_bundle';errors=io.StringIO()
        with contextlib.redirect_stderr(errors):
            rc=mod.main(['--flow',str(self.flow),'--case',str(self.case),'--draft',str(self.draft),'--out',str(out),'--kind','anti-masterprompt'])
        self.assertNotEqual(rc,0)
        self.assertFalse(out.exists())
        self.assertIn('Research flow gate blocked delivery',errors.getvalue())

    def test_claim_links_must_all_have_actually_read_source(self):
        self.start()
        self.cli('read','--flow',self.flow,'--source','S001',
                 '--quote','Erzeuge aus dem Projekt einen wiederverwendbaren Anti-Masterprompt',
                 '--why','First source only')
        self.cli('apply','--flow',self.flow,'--module','context',
                 '--reads','R001','--claims','C001,C002','--effect','revised_claim',
                 '--before','Only initial claim considered',
                 '--after','Claims from both sources assessed',success=False)

    def test_unrelated_same_source_read_is_not_a_claim_anchor(self):
        self.start()
        self.cli('read','--flow',self.flow,'--source','S001',
                 '--quote','Assistent: Ich schlage einen Plugin-Generator vor.',
                 '--why','A separate paragraph in the same original')
        self.cli('apply','--flow',self.flow,'--module','context',
                 '--reads','R001','--claims','C001','--effect','revised_claim',
                 '--before','The user wanted a generator',
                 '--after','The user wanted a masterprompt',success=False)

    def test_tampered_research_claim_read_link_does_not_pass_check(self):
        self.complete()
        state=json.loads(self.flow.read_text())
        state['applications'][1]['reads']=['R001']
        self.flow.write_text(json.dumps(state))
        verdict=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('unread_claim_span:A002:C002',verdict['problems'])

    def test_tampered_read_ranges_are_rechecked_against_original(self):
        self.complete()
        state=json.loads(self.flow.read_text())
        state['reads'][0]['start']=0
        state['reads'][0]['end']=1
        self.flow.write_text(json.dumps(state))
        verdict=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertTrue(any(x.startswith('invalid_recorded_read:') for x in verdict['problems']))

    def test_tampered_quote_hash_is_rejected_at_final_gate(self):
        self.complete()
        state=json.loads(self.flow.read_text())
        state['reads'][1]['quote_sha256']='0'*64
        self.flow.write_text(json.dumps(state))
        verdict=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('invalid_recorded_read:R002',verdict['problems'])

    def test_no_invented_read(self):
        self.start();self.cli('read','--flow',self.flow,'--source','S001','--quote','Ich habe alles gelesen','--why','Wahrscheinlich',success=False)

    def test_missing_research_modules_cannot_pass(self):
        self.start();self.read();res=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('missing_application:reasoning',res['problems'])

    def test_shallow_read_cannot_claim_historical_correction_from_unread_source(self):
        # Stronger mechanical precondition: not even claim-link evidence is allowed
        # if its original text was not seen. Semantic understanding still unproved.
        self.start()
        self.cli('read','--flow',self.flow,'--source','S001',
                 '--quote','Anti-Masterprompt','--why','One tiny excerpt')
        self.cli('apply','--flow',self.flow,'--module','context','--reads','R001',
                 '--claims','C001,C002','--effect','revised_claim',
                 '--before','One passage','--after','Two claims',success=False)

    def test_deep_one_long_original_can_be_mechanically_delivered(self):
        # Historical decisions can appear in one substantial chat; two files aren't a quality measure.
        c=json.loads(self.case.read_text())
        c['sources']=[c['sources'][0]]
        c['claims']=[c['claims'][0]]
        self.case.write_text(json.dumps(c))
        self.draft.write_text('# Relevanter Langzeitstoff\n'+
           ('Aus [[S001]] geht der ursprüngliche Auftrag hervor. Eine spätere Deutung im selben Original '
            'bietet einen Konflikt, dessen Alternativen durch weitere eigene Originallektüre zu prüfen sind. '*4))
        self.start()
        self.cli('read','--flow',self.flow,'--source','S001','--quote','Erzeuge aus dem Projekt','--why','Nutzerwortlaut')
        self.cli('read','--flow',self.flow,'--source','S001','--quote','Ich schlage einen Plugin-Generator vor','--why','Assistentengegenposition')
        for module,effect in [('material','reread'),('context','revised_claim'),('reasoning','competing_hypothesis'),('product','changed_output')]:
            args=['apply','--flow',self.flow,'--module',module,'--reads','R001,R002',
                  '--claims','C001','--effect',effect,'--before','Unterschied fehlt','--after','Unterschied geprüft']
            if module=='product':args+=['--artifact',self.draft]
            self.cli(*args)
        out=self.cli('check','--flow',self.flow,'--draft',self.draft)
        self.assertEqual(out['sources_observed'],1)
        self.assertEqual(out['semantic_quality'],'REQUIRES_REAL_AGENT_REVIEW')

    def test_deep_requires_a_real_cited_anchor_not_fake_number(self):
        self.complete()
        self.draft.write_text(('Der Output hält widersprüchliche Deutungen offen, '
         'aber verliert sämtliche nachprüfbare Herkunft des Materialkörpers. '*5))
        out=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('deep_product_needs_an_actual_source_anchor',out['problems'])

    def test_change_original_forces_new_read(self):
        self.complete();(self.src/'korrektur.md').write_text(self.b+'Änderung')
        self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)

    def test_no_fake_empirical_result(self):
        self.start();self.read()
        self.cli('apply','--flow',self.flow,'--module','lens','--reads','R001','--effect','external_measurement','--before','baseline','--after','intervention',success=False)

    def test_external_artifact_mutation_detected(self):
        self.start();self.read()
        p=self.base/'action.out';p.write_text('observed return code: 0')
        self.apply('execution',effect='observed_action',artifact=p)
        p.write_text('altered')
        res=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('stale_artifact:A001',res['problems'])

    def test_no_execution_without_actual_artifact(self):
        self.start(kind='execution',depth='standard');self.read()
        self.apply('material');self.apply('product')
        res=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('execution_not_observed',res['problems'])

    def test_execution_packaging_requires_existing_verified_result_receipt(self):
        self.start(kind='execution',depth='standard');self.read()
        self.apply('material',effect='reread')
        self.apply('product',effect='changed_output')
        result=self.base/'actual-result.txt'
        result.write_text('Ein tatsächlich durch die Testumgebung geschriebenes Artefakt.',encoding='utf8')
        self.apply('execution',effect='observed_action',artifact=result)
        receipt=self.base/'receipt.json'
        receipt.write_text(json.dumps({'schema':'context-forge-execution-evidence/1',
           'tool':'local test fixture file writer','authorized_scope':'nur Testdatei im TemporaryDirectory',
           'observed_result':'Die angelegte Datei wurde tatsächlich wieder eingelesen',
           'status':'success','result_artifact_path':str(result),
           'result_sha256':hashlib.sha256(result.read_bytes()).hexdigest()}),encoding='utf8')
        pipe=ROOT/'skills/context-forge-ultra/scripts/forge_pipeline.py'
        spec=importlib.util.spec_from_file_location('cfu_execution_pipeline_test',pipe)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        delivered=self.base/'work_delivery';o=io.StringIO();e=io.StringIO()
        with contextlib.redirect_stdout(o),contextlib.redirect_stderr(e):
            rc=mod.main(['--flow',str(self.flow),'--case',str(self.case),
                         '--draft',str(self.draft),'--out',str(delivered),
                         '--kind','execution','--execution-evidence',str(receipt)])
        self.assertEqual(rc,0,e.getvalue())
        self.assertTrue((delivered/'WORK_RESULT.md').exists())
        self.assertFalse((delivered/'sources').exists())
        report=json.loads((delivered/'DELIVERY_CHECK.json').read_text())
        self.assertEqual(report['authorization'],'declared_by_receipt_not_independently_verified')
        self.assertEqual(json.loads(o.getvalue())['host_activation'],'NOT_TESTED')

    def test_execution_refuses_tampered_result(self):
        self.start(kind='execution',depth='standard');self.read()
        self.apply('material');self.apply('product')
        result=self.base/'actual-result.txt';result.write_text('Initial')
        self.apply('execution',effect='observed_action',artifact=result)
        receipt=self.base/'receipt.json'
        receipt.write_text(json.dumps({'schema':'context-forge-execution-evidence/1',
          'tool':'local fixture writer','authorized_scope':'tempdir','observed_result':'readback',
          'status':'success','result_artifact_path':str(result),
          'result_sha256':hashlib.sha256(result.read_bytes()).hexdigest()}))
        result.write_text('Tampered')
        pipe=ROOT/'skills/context-forge-ultra/scripts/forge_pipeline.py'
        spec=importlib.util.spec_from_file_location('cfu_execution_mutation_test',pipe)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        delivered=self.base/'tampered_bundle';stderr=io.StringIO()
        with contextlib.redirect_stderr(stderr):
            rc=mod.main(['--flow',str(self.flow),'--case',str(self.case),
              '--draft',str(self.draft),'--out',str(delivered),
              '--kind','execution','--execution-evidence',str(receipt)])
        self.assertNotEqual(rc,0)
        self.assertFalse(delivered.exists())

    def test_deep_research_without_case_claim_links_is_blocked(self):
        self.start();self.read()
        self.apply('material');self.apply('context');self.apply('reasoning');self.apply('product')
        flow=json.loads(self.flow.read_text())
        for a in flow['applications']:a['claims']=[]
        self.flow.write_text(json.dumps(flow))
        state=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('unbound_research_to_case_claims:reasoning',state['problems'])

    def test_plain_case_need_not_run_complex_research(self):
        self.start(depth='standard');self.read();self.apply('material');self.apply('product',effect='changed_output')
        res=self.cli('check','--flow',self.flow,'--draft',self.draft)
        self.assertEqual(res['status'],'MECHANICALLY_READY_NOT_SEMANTICALLY_VERIFIED')

    def test_secret_in_output_rejected(self):
        self.complete();self.draft.write_text(self.draft.read_text()+'\n-----BEGIN PRIVATE KEY-----')
        res=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('credential_signature_in_product',res['problems'])

    def test_unknown_source_reference_rejected(self):
        self.complete();self.draft.write_text(self.draft.read_text()+'\n[[S999]]')
        res=self.cli('check','--flow',self.flow,'--draft',self.draft,success=False)
        self.assertIn('unknown_source_referenced',res['problems'])

    def test_same_before_after_is_not_application(self):
        self.start();self.read()
        self.cli('apply','--flow',self.flow,'--module','context','--reads','R001','--effect','revised_claim','--before','nichts','--after','nichts',success=False)


if __name__=='__main__':unittest.main()
