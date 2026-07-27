import importlib.util, unittest
from pathlib import Path
SCRIPT=Path(__file__).resolve().parents[1]/"tools/release_gate.py"; spec=importlib.util.spec_from_file_location("gate",SCRIPT); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
class Tests(unittest.TestCase):
 def test_complete_release_passes(self): self.assertTrue(module.evaluate({"controls":{name:True for name in module.REQUIRED}})["ready"])
 def test_missing_control_blocks(self): self.assertIn("rollback_tested",module.evaluate({"controls":{}})["missing"])
if __name__=="__main__": unittest.main()
