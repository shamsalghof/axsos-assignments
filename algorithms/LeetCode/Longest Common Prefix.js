/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let longestCommonPrefix = "";
    for (var i = 0; i < strs[0].length; i++) {
        for (var k = 0; k < strs.length; k++) {
            if (strs[0][i] != strs[k][i]) {
                 return longestCommonPrefix;;
            }
        }
        longestCommonPrefix += strs[0][i];
    }
   
};
