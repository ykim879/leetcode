/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (typeof o1 !== typeof o2) {
        return false
    }
    if (typeof o1 !== "object" || o1 === null || o2 === null) {
        return o1 === o2
    }
    if (Array.isArray(o1) || Array.isArray(o2)) {
        if (Array.isArray(o1) && Array.isArray(o2) && o1.length === o2.length) {
            return o1.every((val, index) => areDeeplyEqual(val, o2[index]));
        }
        return false;
    }
    return Object.keys(o1).every(key => key in o2 && areDeeplyEqual(o1[key], o2[key]));
};
