from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import os
import csv
import datetime

form = 'healthcheck3_202109-202112-2.pdf'
out = 'out.pdf'
data = 'input.csv'

cv = canvas.Canvas(out, pagesize=landscape(A4))

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
cv.setFont('HeiseiMin-W3', 14)

cv.drawString(483, 552, input('学籍番号 '))
cv.drawString(652, 552, input('名前 '))

cv.setFont('HeiseiMin-W3', 8)

TEMP = 130, 515
CHECK = 132, 485
NOTA = 136, 331
YOKO = 42.27
TATE = -15.3
TATET = -15
ROW = 270-515

month = 0

with open(data) as data:
    for row in csv.reader(data):
        date, morning, night, *rest = row
        date = datetime.datetime.strptime(date, '%Y/%m/%d').date()
        if month == 0:
            month = date.month
            assert 9 <= month and month <= 12
        origin_day = 17 if month == 9 else 1
        origin = datetime.date(2021, month, origin_day)
        diff = (date - origin).days
        cdiff = YOKO*(diff % 16), ROW*(diff//16)
        cv.drawString(TEMP[0]+cdiff[0],
                      TEMP[1]+cdiff[1], morning)
        cv.drawString(TEMP[0]+cdiff[0], TEMP[1] +
                      TATET+cdiff[1], night)
        if len(rest) == 0:
            cv.drawString(NOTA[0]+cdiff[0], NOTA[1]+cdiff[1], '■')
        else:
            for sy in rest:
                sy = int(sy)
                cv.drawString(CHECK[0]+cdiff[0],
                              CHECK[1]+cdiff[1]+TATE*sy, '■')

cv.showPage()
cv.save()

res = PdfFileReader(form, strict=False)
res = res.getPage(month - 9)
res.mergePage(PdfFileReader(out).getPage(0))
writer = PdfFileWriter()
writer.addPage(res)
with open(out, 'wb') as out:
    writer.write(out)
