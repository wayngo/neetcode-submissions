class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();  // Create HashSet of Type Integer
        for(int num:nums){   //Iterates through the nums array 
            if(seen.contains(num)){    // if a number previously added to the hashset is found return true
                return true;
            }
            seen.add(num);  //Every iteration add the current num to the hashset
        }
        return false;
    }
}