/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) {
        return []
    }
    adder = 1
    //initialize array with empty array
    res = []
    for (let r = 0; r < rowsCount; r++) {
        res.push(new Array());
    }
    //populate
    for (let i = 0, r = 0; i < this.length; i ++) {
        res[r].push(this[i])
        if (r + adder >= rowsCount || r + adder < 0) {
            adder *= -1
        } else {
            r += adder
        }
    }
    return res

}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
