import unittest, shutil, tempfile
from du import compute_size, BadPathException, parse_args, DEFAULT_BLOCK_SIZE
from os import path


class DuTest(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_path_does_not_exist(self):
        with self.assertRaises(BadPathException):
          entry = compute_size('-a', '123')

    def test_file_size(self):

        file_size = 10000000
        # Create a file in the temporary directory
        with open(path.join(self.test_dir, "temp"), 'w') as f:
          f.write("a" * file_size)

        args = parse_args(["-e", self.test_dir])
        test_file_size = compute_size(args, self.test_dir)
        self.assertEqual(test_file_size, file_size / DEFAULT_BLOCK_SIZE)

if __name__ == '__main__':
   unittest.main()

   