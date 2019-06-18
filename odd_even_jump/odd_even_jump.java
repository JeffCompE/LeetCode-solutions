class Solution {
    // TreeMap solution
    public int oddEvenJumps(int[] A) {
        int length = A.length;
        if (length <= 1) return length;
        TreeMap<Integer, Integer> map = new TreeMap();
        int[] dp_odd = new int[length];
        int[] dp_even = new int[length];
        // initialzie jump on the last index
        dp_odd[length - 1] = dp_even[length - 1] = length - 1;
        // add info on last element to treemap
        map.put(A[length - 1], length - 1);

        for (int i = length - 2; i >= 0; i--) {
            int value = A[i];
            if (map.containsKey(value)) {
                dp_odd[i] = dp_even[map.get(value)];
                dp_even[i] = dp_odd[map.get(value)];
            } else {
                Integer largest_in_less_than = map.lowerKey(value);
                if (largest_in_less_than != null) dp_even[i] = dp_odd[map.get(largest_in_less_than)];

                Integer smallest_in_greater_than = map.higherKey(value);
                if (smallest_in_greater_than != null) dp_odd[i] = dp_even[map.get(smallest_in_greater_than)];
            }
            map.put(value, i);
        }

        int count = 0;
        for (int jump: dp_odd)
            if (jump > 0) count++;
        return count;
    }
}
