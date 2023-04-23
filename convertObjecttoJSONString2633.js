/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (typeof object === "string") {
        return '"' + object + '"';
    }
    if (typeof object !== "object" || object === null) {
        return object;
    }
    if (Array.isArray(object)) {
        res = "[";
        for (let v of object) {
            res += jsonStringify(v);
            res += ','
        }
        return res.length > 1 ? res.slice(0, -1) + "]" : res + "]";
    }
    res = "{"
    for (let key of Object.keys(object)) {
        res += ('"' + key + '"' + ":" + jsonStringify(object[key]))
        res += ","
    }
    return res.length > 1 ? res.slice(0, -1) + "}" : res + "}"

};
