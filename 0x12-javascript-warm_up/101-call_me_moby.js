#!/usr/bin/node

module.exports.callMeMoby = function callMeMoby (n, f) {
  for (let idx = 0; idx < n; idx++) {
    f();
  }
};
