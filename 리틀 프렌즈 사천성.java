import java.util.*;

class Solution {

	public String solution(int m, int n, String[] board) {
		StringBuilder answer = new StringBuilder();
		
		// 알파벳 A부터 Z까지의 좌표를 저장하는 배열
		// { 첫번째 A의 행, 첫번째 A의 열, 두번째 A의 행, 두번째 A의 열 }
        	int[][] alphaCoor = new int[26][4];
        	for (int[] a : alphaCoor)
        		Arrays.fill(a, -1);

        	// 알파벳이 제거 가능한지 나타내는 배열
        	// 0: 제거 가능한지 체크안했음, 1: 체크했음, 제거 불가능, 2: 제거 가능
        	int[] removePossible = new int[26];
        
        	// board 나타내는 2차원 배열
        	char[][] grid = new char[m][n];
        
        	// board에 있는 알파벳의 개수
        	int alphaCount = 0;
        
        	// board를 grid에 옮김. 알파벳을 발견하면 alphaCoor에 좌표를 저장하고 alphaCount를 증가시킴 
        	for (int i = 0 ; i < m; i++) {
        		for (int j = 0; j < n; j++) {
        			char c = board[i].charAt(j);
        			grid[i][j] = c;
        			if (c != '.' && c != '*') {
        				alphaCount++;
        				if (alphaCoor[c - 'A'][0] == -1) {
        					alphaCoor[c - 'A'][0] = i;
            				alphaCoor[c - 'A'][1] = j;
        				}
        				else {
        					alphaCoor[c - 'A'][2] = i;
            				alphaCoor[c - 'A'][3] = j;
        				}
        			}
        		}
        	}
		
        	// 같은 알파벳이 2개씩 있으므로 alphaCount를 2로 나눠줌 
        	alphaCount /= 2;
        
        	// alphaCount가 0보다 클때까지
		while (alphaCount > 0) {
			for (int i = 0 ; i < m; i++) {
	        		for (int j = 0; j < n; j++) {
	        			char c = grid[i][j];
	        			// c가 알파벳이라면
	        			if (c != '.' && c != '*') {
	        				// c를 제거 가능한지 체크안했다면
	        				if (removePossible[c - 'A'] == 0) {
	        					// 제거 가능한지 체크
	        					int x1 = alphaCoor[c - 'A'][0];
	        					int y1 = alphaCoor[c - 'A'][1];
	        					int x2 = alphaCoor[c - 'A'][2];
	        					int y2 = alphaCoor[c - 'A'][3];
	        				
	        					// 제거 가능한지 나타내는 변수
	        					boolean flag = true;
	        				
	        					if(x1 == x2) {
	        						for (int k = y1; k <= y2; k++) {
	        							if (grid[x1][k] != '.' && grid[x1][k] != c) {
	        								flag = false;
	        								break;
	        							}
	        						}
	        					}
	        					else {
	        						if (y1 == y2) {
	        							for (int k = x1; k <= x2; k++) {
		        							if (grid[k][y1] != '.' && grid[k][y1] != c) {
		        								flag = false;
		        								break;
		        							}
		        						}
	        						}
	        						else {
	        							if (y1 < y2) {
	        								for (int k = y1; k <= y2; k++) {
	    	        								if (grid[x1][k] != '.' && grid[x1][k] != c) {
	    	        									flag = false;
	    	        									break;
	    	        								}
	    	        							}
	        								for (int k = x1; k <= x2; k++) {
			        							if (flag == false) break;
	        									if (grid[k][y2] != '.' && grid[k][y2] != c) {
	        										flag = false;
	        										break;
	        									}
			        						}
	        								if (flag == false) {
	        									flag = true;
	        									for (int k = x1; k <= x2; k++) {
		        									if (grid[k][y1] != '.' && grid[k][y1] != c) {
		        										flag = false;
		    	        								break;
		        									}
				        						}
		        								for (int k = y1; k <= y2; k++) {
		        									if (flag == false) break;
		    	        								if (grid[x2][k] != '.' && grid[x2][k] != c) {
		    	        									flag = false;
		        										break;
		    	        								}
		    	        							}
	        								}
	        							}
	        							else {
	        								for (int k = y1; k >= y2; k--) {
	    	        								if (grid[x1][k] != '.' && grid[x1][k] != c) {
	    	        									flag = false;
	    	        									break;
	    	        								}
	    	        							}
	        								for (int k = x1; k <= x2; k++) {
	        									if (flag == false) break;
			        							if (grid[k][y2] != '.' && grid[k][y2] != c) {
			        								flag = false;
	    	        									break;
			        							}
			        						}
	        								if (flag == false) {
	        									flag = true;
	        									for (int k = x1; k <= x2; k++) {
				        							if (grid[k][y1] != '.' && grid[k][y1] != c) {
				        								flag = false;
		    	        									break;
				        							}
				        						}
		        								for (int k = y1; k >= y2; k--) {
		        									if (flag == false) break;
		    	        								if (grid[x2][k] != '.' && grid[x2][k] != c) {
		    	        									flag = false;
		    	        									break;
		    	        								}
		    	        							}
	        								}
	        							}
	        						}
	        					}
	        				
	        					// 제거 가능하다면
	        					if (flag == true) removePossible[c - 'A'] = 2;
	        					// 제거 불가능하다면
	        					else removePossible[c - 'A'] = 1; // 체크했다는 표시를 함	        				
	        				
	        				}
	        			}
	        		}
	        	}
			
			// 제거가능한게 없는지 나타내는 변수
			boolean isImpossible = true;
			
			// 체크했지만 제거 불가능했던 것은 체크안한 상태로 되돌림
			for (int k = 0; k < 26; k++) {
				if (removePossible[k] == 1) removePossible[k] = 0;
			}
			
			// 제거가능한 것들중 알파벳 순으로 가장 먼저인 것을 찾아 제거
			for (int k = 0; k < 26; k++) {
				if (removePossible[k] == 2) {
					grid[alphaCoor[k][0]][alphaCoor[k][1]] = '.';
					grid[alphaCoor[k][2]][alphaCoor[k][3]] = '.';
					alphaCount--;
					answer.append((char) (k + 'A'));
					removePossible[k] = 0;
					isImpossible = false; // 제거 가능한게 있었음
					break;
				}
			}
			
			// 제거가능한게 없었으면
			if (isImpossible) return "IMPOSSIBLE";
		}
		
		// 결과 리턴
        	return answer.toString();
    	}

}
