from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from morph import init, check

class MorphTests(unittest.TestCase):
    def test_init_check(self):
        with TemporaryDirectory() as t:
            p=Path(t)/'case'
            init(p)
            self.assertIn('INCOMPLETE',check(p))
            with self.assertRaises(ValueError): init(p)
            for file in p.glob('*.md'):
                file.write_text(file.read_text().replace('TODO','Filled'),encoding='utf-8')
            self.assertIn('READY',check(p))
    def test_missing(self):
        with TemporaryDirectory() as t:
            self.assertIn('MISSING', check(t))

if __name__=='__main__': unittest.main()
