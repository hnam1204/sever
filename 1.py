# up code này lên github chẳng hạn (nhớ enc)
code = """
status = True
"""
exec(code)

if status:
	pass
else:
	exit()
# muốn đóng server thì status = False sau đó update lại file trên github, chờ tầm 5 phút cho github load run tool main = exit :))
# đây là cách đơn giản nhất (có thể bị bypass)
