// 완주하지 못한 선수
import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
		HashMap<String, Integer> hm = new HashMap<>();
		
		for (String part : participant) {
			if (hm.get(part) == null) {
				hm.put(part, 1);
			}
			else {
				hm.put(part, hm.get(part) + 1);
			}
		}

		for (String comp : completion) {
			if (hm.get(comp) != null) {
				hm.put(comp, hm.get(comp) - 1);
			}
		}

		for (String key : hm.keySet()) {
			if (hm.get(key) == 1) {
				return (key);
			}
		}
        return "";
    }
}