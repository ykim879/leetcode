 /**
 * @param {Function} fn
 */
function memoize(fn) {
    var d = new Object();
    var callCount = 0; 
    return function(...args) {
        key = args.join("-");
        if (d[key] === undefined) {
            d[key] = fn(...args);
        }
        return d[key] 
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
