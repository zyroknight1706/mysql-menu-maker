from fpdf import FPDF
import webbrowser

#for creating the pdf
def createpdf(data_dict):
    
    #courses = ['b', 'l', 'd']
    data_list = [['Day: ', 'Breakfast', 'Lunch', 'Dinner']]
    #write data in a more accessible format
    for i in data_dict:
        data_row = []
        data_row.append(i)
        data_row.append(data_dict[i]['b'])
        data_row.append(data_dict[i]['l'])
        data_row.append(data_dict[i]['d'])
        data_list.append(data_row)

    pdf = FPDF(orientation='l')

    pdf.add_page()

    pdf.set_font('Arial', '', 20.0)

    epw = pdf.w - 2*pdf.l_margin

    col_width = epw/4

    pdf.cell(epw, 0.0, 'Menu for the week: ', align='C')
    pdf.ln(20.0)

    pdf.set_font_size(15.0)

    th = pdf.font_size

    for r in data_list:
        for c in r:
            pdf.cell(col_width, 3*th, c, border=1,align='C')
        pdf.ln(2*th)

    pdf.output('output.pdf')
    showpdf()
    return True
def showpdf():
    webbrowser.open_new('output.pdf')
