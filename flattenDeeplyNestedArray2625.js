/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    var flatten = function (depth, res, item) {
        //pop and concat to res if it is is array flatten recursively
        for (let i of item) {
            if (depth > 0 && Array.isArray(i)) {
                flatten(depth - 1, res, i);
            } else {
                res.push(i);
            }
        }
        return res;
    };
    res = [];
    return flatten(n, res, arr);
};
