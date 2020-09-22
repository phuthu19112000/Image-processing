# import the necessary packages
import cv2

class ShapeDetector:

	def detect(self, c):
		# khởi tạo tên hình dạng và xấp xỉ đường viền
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		# Nếu hình là một hình tam giác, nó sẽ có 3 đỉnh
		if len(approx) == 3:
			shape = "Tam giac"

		# nếu hình có 4 đỉnh thì nó là hình vuông hoặc 
        # hình chữ nhật
		elif len(approx) == 4:
			# tính hộp giới hạn của đường viền và sử dụng hộp giới hạn 
            # để tính tỷ lệ khung hình
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# một hình vuông sẽ có tỷ lệ khung hình xấp xỉ bằng một, 
            # nếu không, hình dạng là một hình chữ nhật
			shape = "vuong" if ar >= 0.95 and ar <= 1.05 else "chu nhat"

		# Nếu hình dạng là một hình ngũ giác, nó sẽ có 5 đỉnh
		elif len(approx) == 5:
			shape = "ngu giac"

		# mặt khác, chúng ta giả sử hình dạng là một vòng tròn
		else:
			shape = "tron"

		# return the name of the shape
		return shape