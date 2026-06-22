class Solution {
    private List<Integer> lenPrefixList;

    public Solution() {
        lenPrefixList = new ArrayList<>();
    }

    public String encode(List<String> strs) {
        for (String str : strs) {
            lenPrefixList.add(str.length());
        }

        return String.join("", strs);
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        int startIdx = 0;
        int endIdx = 0;

        for (Integer length : lenPrefixList) {
            startIdx = endIdx;
            endIdx = startIdx + length;

            strs.add(str.substring(startIdx, endIdx));
        }

        return strs;
    }
}
