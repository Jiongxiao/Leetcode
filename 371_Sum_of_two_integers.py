class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b==0:
        	return a
        else:
        	return self.getSum(a^b,(a&b)<<1)

####仿佛python里证书的位数是无限的，因此遇到负数的时候，递归就无限了！！！！java和c++下都是可以的

a=5
b=-2



###########以下是java解法
public class GetSum{
	public static void main(String[] args) {
		int a=5,b=-2;
		getSum(a,b);

	}
	static int getSum(int a, int b){
		if(b==0) return a;
		else {
			int c=(a&b)<<1;
			int d=a^b;
			System.out.println(d+","+ c);
			return getSum(a^b,(a&b)<<1);
		}
	}
}