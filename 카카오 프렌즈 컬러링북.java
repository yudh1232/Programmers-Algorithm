import java.util.*;

class Solution {
    
  static int a, b;
	static int[][] pictureCopy;
	static int[][] area;
	static boolean[][] visited;
	static int areaNumber;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	public static int[] solution(int m, int n, int[][] picture) { 
        a = m;
        b = n;
        pictureCopy = new int[m][n];
        area = new int[m][n]; // 번호로 각 영역을 나타낼 배열
        visited = new boolean[m][n];
        
        areaNumber = 1; // 영역의 번호
        int areaCnt = 0; // 영역의 수
        
        // picture을 pictureCopy에 복사, picture에서 0인 부분은 방문 처리함
        for (int i = 0; i < m; i++) {
        	for (int j = 0; j < n; j++) {
        		pictureCopy[i][j] = picture[i][j];
        		if (picture[i][j] == 0) visited[i][j] = true;
        	}
        }
        
        // 방문하지 않았다면 dfs진행
        // 방문하지 않은 칸을 발견할 때마다 영역의 칸수와 영역의 번호를 증가시킴
        for (int i = 0; i < m; i++) {
        	for (int j = 0; j < n; j++) {
        		if (!visited[i][j]) {
        			dfs(i, j);
        			areaCnt++;
        			areaNumber++;
        		}
        	}
        }
        
        // arr 배열에 각 영역별 칸 수를 넣음 
        int[] arr = new int[areaCnt + 1];
        for (int i = 0; i < m; i++) {
        	for (int j = 0; j < n; j++) {
        		if (area[i][j] != 0) arr[area[i][j]]++;
        	}
        }
        
        // 최대값을 구하기 위해 정렬
        Arrays.sort(arr);
        
        // 결과 리턴
        int[] answer = new int[2];
        answer[0] = areaCnt;
        answer[1] = arr[areaCnt];
        return answer;
    }
	
	private static void dfs(int x, int y) {
		// 방문표시, 영역 번호 표시
		visited[x][y] = true;
		area[x][y] = areaNumber;
		
		// 가능한 위치로 dfs 진행
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (nx < 0 || nx >= a || ny < 0 || ny >= b) continue;
			if (visited[nx][ny]) continue;
			if (pictureCopy[nx][ny] != pictureCopy[x][y]) continue;
			dfs(nx, ny);			
		}
	}
    
}
