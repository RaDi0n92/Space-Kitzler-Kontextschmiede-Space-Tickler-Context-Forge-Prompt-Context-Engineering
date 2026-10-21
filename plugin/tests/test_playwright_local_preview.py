"""Local *output preview* only; cannot establish authenticated ChatGPT host activation."""
import html
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))

class BrowserPreviewTest(unittest.TestCase):
    def test_playwright_actual_output_preview(self):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            self.skipTest('Playwright unavailable')
        # Import inside the test: exporting unittest.TestCase as a module global
        # causes pytest to collect the entire research suite a second time.
        from test_research_flow import ResearchFlowTests
        fx=ResearchFlowTests('test_deep_research_flow_goes_from_sources_to_actual_product')
        fx.setUp()
        try:
            result=fx.complete()
            pipeline=fx.base/'bundle_for_browser'
            script=Path(__file__).resolve().parents[1]/'skills/context-forge-ultra/scripts/forge_pipeline.py'
            spec=importlib.util.spec_from_file_location('browser_forge_pipeline',script)
            runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
            with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(runner.main(['--flow',str(fx.flow),'--case',str(fx.case),
                  '--draft',str(fx.draft),'--out',str(pipeline),'--kind','anti-masterprompt']),0)
            product=(pipeline/'ANTI_MASTERPROMPT.md').read_text()
            delivery=json.loads((pipeline/'DELIVERY_CHECK.json').read_text())
            self.assertEqual(delivery['source_transfer'],'references_only_not_access_grant')
            self.assertFalse((pipeline/'sources').exists())
            flow=json.loads(fx.flow.read_text())
            status=html.escape(result['status'])
            content=html.escape(product)
            sources=', '.join(sorted({x['source'] for x in flow['reads']}))
            pagehtml=f'''<!doctype html><html lang="de"><meta charset="utf-8"><title>Context Forge · lokale Ergebnisprobe</title>
            <body><main><h1>Context Forge · lokale Ergebnisprobe</h1>
            <p id="gate-status">{status}</p><button id="toggle" aria-expanded="false">Quellen anzeigen</button>
            <aside id="sources" hidden>Prüfte Originalanker: {html.escape(sources)}</aside>
            <article id="product"><pre>{content}</pre></article></main>
            <script>document.querySelector('#toggle').onclick=()=>{{let e=document.querySelector('#sources');e.hidden=!e.hidden;document.querySelector('#toggle').setAttribute('aria-expanded',String(!e.hidden))}}</script>
            </body></html>'''
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
                page=browser.new_page(viewport={'width':1280,'height':720})
                page.set_content(pagehtml)
                self.assertEqual(page.title(),'Context Forge · lokale Ergebnisprobe')
                self.assertIn('MECHANICALLY_READY_NOT_SEMANTICALLY_VERIFIED',page.locator('#gate-status').inner_text())
                self.assertIn('Spätere Korrektur [[S002]]',page.locator('#product').inner_text())
                self.assertFalse(page.locator('#sources').is_visible())
                page.get_by_role('button',name='Quellen anzeigen').click()
                self.assertTrue(page.locator('#sources').is_visible())
                self.assertIn('S001, S002',page.locator('#sources').inner_text())
                self.assertEqual(page.locator('#toggle').get_attribute('aria-expanded'),'true')
                browser.close()
        finally:
            fx.doCleanups()

if __name__=='__main__':unittest.main()
