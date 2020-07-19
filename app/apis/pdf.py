import fitz ## this fitz for pdf is different check during pip install
from flask_appbuilder.api import BaseApi, expose
from app import appbuilder


class PDFApi(BaseApi):
	@expose('/sign_pdf')
	def greeting(self):
		input_file = "/home/sudhir/smartterra/aquaMl/app/apis/sudhir.pdf"
		output_file = "/home/sudhir/smartterra/aquaMl/app/apis/example-with-barcode.pdf"
		barcode_file = "/home/sudhir/smartterra/aquaMl/app/apis/sign.png"

		# define the position (upper-right corner)
		image_rectangle = fitz.Rect(450, 20, 550, 120)

		# retrieve the first page of the PDF
		file_handle = fitz.open(input_file)
		first_page = file_handle[0]

		# for page in file_handle:


		# add the image
		first_page.insertImage(image_rectangle, pixmap = fitz.Pixmap(barcode_file))

		file_handle.save(output_file)
		return self.response(200, message="Hello")


appbuilder.add_api(PDFApi)
