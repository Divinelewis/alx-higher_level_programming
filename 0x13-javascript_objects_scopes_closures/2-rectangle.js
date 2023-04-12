#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // if the input is invalid, it returns an empty object
    }
    this.width = w;
    this.height = h;
  }
}
