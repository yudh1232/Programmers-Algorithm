class Solution {
    
	static int answer;
	static char[] input;
	static char[] arrangement;
	static boolean[] isSelected;
	
	public int solution(int n, String[] data) {
        input = new char[] {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
		arrangement = new char[8]; // 순서배치를 나타내는 배열
		isSelected = new boolean[8]; // 순열을 뽑을때 사용하는 배열
		answer = 0;
		
		// 순서배치하기
		setIn(0, n, data);
		
		// 결과 리턴
        return answer;
    }

	private static void setIn(int cnt, int n, String[] data) {
		// 순서배치를 마쳤으면 조건에 맞는지 체크하러 감
		if (cnt == 8) {
			check(n, data);
			return;
		}
		
		// 순서배치하기
		for (int i = 0; i < 8; i++) {
			if (isSelected[i]) continue;
			
			arrangement[cnt] = input[i];
			isSelected[i] = true;
			
			setIn(cnt + 1, n, data);
			
			isSelected[i] = false;
		}
	}

	private static void check(int n, String[] data) {
		String s = String.valueOf(arrangement);

		// n가지 조건을 모두 만족하는지 체크
		for (int i = 0; i < n; i++) {
			int a = s.indexOf(data[i].substring(0, 1));
			int b = s.indexOf(data[i].substring(2, 3));
			
			char condition = data[i].charAt(3);
			int gap = data[i].charAt(4) - '0';
			
			if (condition == '>') {
				if (Math.abs(a - b) - 1 <= gap) return;
			}
			else if (condition == '<') {
				if (Math.abs(a - b) - 1 >= gap) return;
			}
			else { // condition == '='
				if (Math.abs(a - b) - 1 != gap) return;
			}
		}
		
		// n가지 조건을 모두 만족하면 경우의 수 1 증가시킴
		answer++;
	}
  
}
