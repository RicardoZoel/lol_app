import io
import base64
from odoo import models, fields, api, exceptions


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
                elements = line.split(';')
                if len(elements) > 1:
                    self.env['lol_app.elos_model'].create({
                        'name': elements[0],
                        'elo': float(elements[1])
                    })

    def _read_file_from_binary(self, file):
        try:
            with io.BytesIO(base64.b64decode(file)) as f:
                f.seek(0)
                return f.read().decode('UTF-8')
        except Exception as e:
            print(str(e))
            raise e