public class Solution {
    public int[][] reconstructQueue(int[][] people) {
        int n=people.length;
        Arrays.sort(people,new Comparator<int[]>(){
           @Override
           public int compare(int[] o1, int[] o2){
               return o1[0]!=o2[0]?-o1[0]+o2[0]:o1[1]-o2[1];
           }
        });
            List<int[]> list=new LinkedList<int[]>();
            for (int i=0;i<n;i++){
                list.add(people[i][1],people[i]);
            }
            return list.toArray(new int[n][]);  ///////Important hehre!!
    }
}