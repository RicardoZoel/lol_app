import io
import base64
from numpy import integer
from odoo import models, fields, exceptions


class UploadFile(models.TransientModel):
    _name = 'lol_app.upload_file'

    upload_file = fields.Binary(string='Upload file', required=True)
    file_name = fields.Char(string='Filename')

    def import_file(self):
        if self.file_name:
            if '.csv' not in self.file_name:
                raise exceptions.ValidationError('File must be a CSV')
            file = self._read_file_from_binary(self.upload_file)
            lines = file.split('\n')
            for line in lines:
                elements = line.split(',')
                elos=elements[1].split(';')
                if len(elements) > 1:
                    self.env.cr.execute("INSERT INTO lol_app_elos_model(id, name,value) values("+elements[0]+",'"+elements[0]+"',"+elements[2]+")" )
                    for elo in elos:
                        self.env.cr.execute("INSERT INTO lol_app_elo_model2elos_model values("+elo+","+elements[0]+")" )
                    #insert into lol_app_elo_model2elos_model values (5,1);
                    #self.env['lol_app.elos_model'].create({
                    #    'name': elements[0],
                    #    'elo': [elos[0],elos[1],elos[2],elos[3],elos[4],elos[5]],
                    #    'value': int(elements[2])
                    #})

    def _read_file_from_binary(self, file):
        try:
            with io.BytesIO(base64.b64decode(file)) as f:
                f.seek(0)
                return f.read().decode('UTF-8')
        except Exception as e:
            print(str(e))
            raise e