import gtk

class Window(gtk.Window):
	'''an example window'''


	def __init__(self):
		gtk.Window.__init__(self)
		self.set_title("ejemplo loco")
		self.set_default_size(400, 300)
		self.set_border_width(4)

		self.count = 0

		vbox = gtk.VBox()
		bbox = gtk.HButtonBox()

		self.label = gtk.Label("hola mundo")
		image = gtk.image_new_from_file("winlogo.gif")

		ok_btn = gtk.Button(stock=gtk.STOCK_OK)
		cancel_btn = gtk.Button(stock=gtk.STOCK_CANCEL)

		bbox.pack_start(ok_btn)
		bbox.pack_start(cancel_btn)

		vbox.pack_start(self.label, True, True)
		vbox.pack_start(image, False)
		vbox.pack_start(bbox, False)

		self.add(vbox)
		vbox.show_all()

		self.connect('delete-event', gtk.main_quit)
		ok_btn.connect('clicked', self._on_ok_clicked)
		cancel_btn.connect('clicked', gtk.main_quit)

	def _on_ok_clicked(self, button):
		'''callback called when ok_button is clicked'''
		self.count += 1
		self.label.set_text("hola mundo %d" % self.count)


if __name__ == '__main__':
	Window().show()
	gtk.main()
