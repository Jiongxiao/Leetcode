public class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int n=points.length;
        int res=0;
        if (n<3) return 0;
        for (int i=0;i<n;i++){
            Map <Integer,Integer> map= new HashMap<>();
            for (int j=0; j<n; j++){
                int dis=(points[i][0]-points[j][0])*(points[i][0]-points[j][0])
                +(points[i][1]-points[j][1])*(points[i][1]-points[j][1]);
                map.put(dis,map.getOrDefault(dis,0)+1);
            }
            Iterator iter=map.entrySet().iterator();
            while(iter.hasNext()){
                Map.Entry entry=(Map.Entry) iter.next();
                int val= (int) entry.getValue();
                // System.out.println(val);
                if (val>=2){
                    res+=val*(val-1);
                }
            }
        }

        return res;
    }
}


public class Solution{
    public int numberOfBoomerangs(int[][] points){
        int n= points.length;
        int res=0;
        if (n<3) return 0;
        Map <Integer,Integer> map= new HashMap<>();
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                int dis=(points[i][0]-points[j][0])*(points[i][0]-points[j][0])
                +(points[i][1]-points[j][1])*(points[i][1]-points[j][1]);
                map.put(dis,map.getOrDefault(dis,0)+1);
            }
            for (int val: map.values()){
                res+=val*(val-1);
            }
            map.clear();
        }
        return res;
    }
}