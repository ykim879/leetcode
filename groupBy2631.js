/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    let d = {};
    for (const v of this) {
        res = fn(v);
        if (d[res]) {
            d[res].push(v);
        } else {
            d[res] = [v]
        }
    }
    return d
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
