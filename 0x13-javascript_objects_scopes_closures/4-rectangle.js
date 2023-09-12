#!/usr/bin/node
class Rectangle {
	constructor(w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}

	}
	print () {

		for (let b = 0; b < this.width; b++) {
			let b = '';

		for (let c = 0; c < this.height; c++) {
			b += 'x';
	}
		console.log(b);
	}
}

	rotate () {
		const rot = this.width;
		this.width = this.height;
		this.height = rot;
}

	double () {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
