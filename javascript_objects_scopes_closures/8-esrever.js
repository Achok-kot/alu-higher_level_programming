#!/usr/bin/node
exports.esrever = function (list) {
  if (list.length === 0) return [];
  return [list[list.length - 1]].concat(exports.esrever(list.slice(0, -1)));
};

