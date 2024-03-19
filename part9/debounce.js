/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let id
    cleartimeout(id)
    id = setTimeout(() => {
      fn()
    }, t);

  return function(...args) {
      
  }
};

