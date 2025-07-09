from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
import random 
from kivy.uix.button import Button

# RGBA = RED, green, blue, opacity
Window.clearcolor = (1, 1, 1, 1)

class PaintWindow(Widget):
	def on_touch_down(self, touch):
		colorR = random.randint(0, 255)
		colorG = random.randint(0, 255)
		colorB = random.randint(0, 255)
		self.canvas.add(Color(rgb=(colorR/255.0, colorG/255.0, colorB/255.0)))
		touch.ud['line'] = Line(points=(touch.x, touch.y))
		self.canvas.add(touch.ud['line'])
		
	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]
	
# Root window = paint window + Button
class PaintApp(App):
	def build(self):
		
		rootWindow = Widget()
		self.painter = PaintWindow()
		ClearnBtn = Button(text='Clear')
		ClearnBtn.bind(on_release=self.Clear_canvas)
		rootWindow.add_widget(self.painter)
		rootWindow.add_widget(ClearnBtn)
		return rootWindow
		
	def Clear_canvas(self, obj):
		self.painter.canvas.clear()
		
PaintApp().run()