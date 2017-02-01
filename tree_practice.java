
class Node {
    int data;
    Node left;
    Node right;
}



void preOrder(Node root) {
    System.out.print(root.data + " ");
    if(root.left!=null)preOrder(root.left);
    if(root.right!=null)preOrder(root.right);
}

void postOrder(Node root) {
    if(root.left!=null)postOrder(root.left);
    if(root.right!=null)postOrder(root.right);
    System.out.print(root.data + " ");
    

}
void inOrder(Node root) {
    
    if(root.left!=null)inOrder(root.left);
    System.out.print(root.data + " ");
    if(root.right!=null)inOrder(root.right);
}
static int height(Node root) {
  	// Write your code here.
    int answer = 0;
    root.data = 0;
    LinkedList<Node> q = new LinkedList<Node>();
    q.add(root);
    while(!q.isEmpty()){
        Node head = q.remove();
        if(head.left!=null){
            head.left.data = head.data+1;
            q.add(head.left);
            answer = head.left.data;
        }
        if(head.right!=null){
            head.right.data = head.data+1;
            q.add(head.right);
            answer = head.right.data;
        }
    }
    return answer;
}
void top_view(Node root)
{
    left_view(root);
    right_view(root);
}
void left_view(Node root){
    if(root.left!=null) left_view(root.left);
    System.out.print(root.data + " ");
}
void right_view(Node root){
    
    while(root.right!=null){
        System.out.print(root.right.data + " ");
        root = root.right;
    } 
}
void LevelOrder(Node root)
{
  LinkedList<Node> q = new LinkedList<Node>();
  q.add(root);
 
  while(!q.isEmpty()){
        Node head = q.remove();
        System.out.print(head.data+ " ");
        if(head.left!=null){              
            q.add(head.left);
        }
        if(head.right!=null){
            q.add(head.right);
        }
    }
  
}
static Node Insert(Node root,int value)
{
    Node newNode = new Node();
    newNode.data = value;
    Node answer = root;
    if(root == null) return newNode;   
    while(true){
        if(value < root.data){
            if(root.left==null)
            {
                root.left = newNode;
                return answer;
            }
            else root = root.left;
        }
        if(value > root.data){
            if(root.right==null)
                {
                root.right = newNode;
                return answer;
            }
            else root = root.right;
        }
    }       
}
/*  
class Node
   public  int frequency; // the frequency of this tree
    public  char data;
    public  Node left, right;
 
*/ 

void decode(String S ,Node root){
 int position = 0;
 String answer = "";
 Node start = root;
 while(position < S.length()){
     int one_or_zero = Integer.valueOf(S.charAt(position));
     position++;
     if(one_or_zero == 49){ //move right apparently Integer.valueOf gets ascii representation
         if(root.right!=null){
            root = root.right; 
            if(root.left == null && root.right == null){
                answer+= Character.toString(root.data);
                root = start;
            } 
         }       
     }
     if(one_or_zero == 48){ //move left
         if(root.left!=null){
            root = root.left; 
            if(root.left == null && root.right == null){
                answer+= Character.toString(root.data);
                root = start;
            } 
         }       
     }
 }
 System.out.print(answer);
 
}
static Node lca(Node root,int v1,int v2)
{
    while(true){
        if(v1 == root.data || v2 == root.data) return root;
        if((v1 < root.data && v2 > root.data) || (v2 < root.data && v1 > root.data)) return root;
        else if ( v1< root.data && v2 < root.data){
            root = root.left;
        }
        else if( v1 > root.data && v2 > root.data){
            root = root.right;
        } 
    }
   
}


