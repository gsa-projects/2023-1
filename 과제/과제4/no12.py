files = ['pro.gif', 'tt.png', 'q1.jpg', 'melon.gif', 'q2.hwp', 'j3.ppt', 'table.xslx', 'spc.docx', 'gsa.jpg']
print(list(filter(lambda name: name.split('.')[1] in ['jpg', 'gif'], files)))