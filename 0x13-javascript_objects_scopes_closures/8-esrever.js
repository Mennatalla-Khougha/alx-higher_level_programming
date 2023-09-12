#!/usr/bin/node

exports.esrever = function (list) {
  const lst = [];

  for (let i = list.length - 1, j = 0; i >= 0; --i, j++) {
    lst[j] = list[i];
  }
  return lst;
};
