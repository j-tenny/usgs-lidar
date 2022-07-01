import pdalpipe.readers
import pdalpipe.writers
import pdalpipe.filters

def stringify_bounds(bounds):
    return f'([{bounds[0]},{bounds[2]}],[{bounds[1]},{bounds[3]}])'

class Pipeline(list):
    def __init__(self,*args):
        super().__init__(*args)

    def to_json_string(self):
        import json
        return json.dumps(self)

    def to_json_file(self,path):
        import json
        with open(path,'w') as f:
            f.write(json.dumps(self))

    def to_json_tempfile(self):
        import tempfile
        file = tempfile.NamedTemporaryFile().name
        self.to_json_file(file)
        return file

    def execute(self):
        import pdal
        pipe = pdal.Pipeline(self.to_json_string())
        pipe.execute()
        return pipe

    def execute_subprocess(self):
        import subprocess
        file = self.to_json_tempfile()
        subprocess.run('pdal','pipeline',file)