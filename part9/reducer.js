/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  let final = init
  nums.forEach((val) => 
    {
      const mapped_val = fn(val)
      final += mapped_val
    }
  )
  return final
    
};