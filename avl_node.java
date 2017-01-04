package artificial;

import java.util.LinkedList;

class Node{
   int val;   //Value
   int ht;      //Height
   Node left;   //Left child
   Node right;   //Right child

Node(){
	this.val = -1;
	this.ht = -1;
	this.left= null;
	this.right = null;
}
Node(int v, int h, Node l, Node r){
	this.val =v;
	this.ht = h;
	this.left=l;
	this.right=r;
}

static Node insert(Node root,int val)
{
   
  
   Node head = root;
   int prev_head_balance = head.left.ht-head.right.ht;
   while(true){
       // code the cases where we do not disrupt avl first
       if(val < head.val){
           if(head.left == null){ // we are able to insert without disrupting avl
               head.left = new Node();
               head.left.val = val;
               head.left.ht = head.ht-1;
               return root;
           }
           else{ // we are not able to insert without disrupting avl unless bf was 0
               if(prev_head_balance == 0){
                   if(val < head.left.val){
                       if(head.left.left!=null){
                           head = head.left;
                           continue;
                       }
                       head.left.left.val =val;
                   } // inner if
                   else {
                       if(head.left.right!=null){
                           head = head.left;
                           continue;
                       }
                       head.left.right = new Node();
                       head.left.right.val =val;
                       head.left.right.ht =head.left.ht-1;
                   } //inner else
               }//outer if
               
               else{ // this is the case where we needed to insert to make avl but now we are violating
                   if(val<head.left.left.val){
                       if(head.left.left.left != null){
                           head=head.left;
                           continue;
                       }
                       head.left.left.left = new Node();
                       head.left.left.left.val =val;
                       head.left.left.left.ht = head.left.left.ht-1;
                       leftLeft(head);
                       return root;
                   }
                   else{
                       if(head.left.left.right !=null){
                           head = head.left;
                           continue;
                       }
                       head.left.left.right = new Node();
                       head.left.left.right.val = val;
                       head.left.left.right.ht = head.left.left.ht-1;
                       leftRight(head);
                       return root;
                   } 
                   
                   
               }
           }
       } // outer if
           // Symmetric, replace all < with >
       if(val > head.val){
           if(head.right == null){ // we are able to insert without disrupting avl
               head.right = new Node();
               head.right.val = val;
               head.right.ht = head.ht-1;
           }
           else{ // we are not able to insert without disrupting avl unless bf was 0
               if(prev_head_balance == 0){
                   if(val > head.right.val){
                       if(head.right.right!=null){
                           head = head.right;
                           continue;
                       }
                       head.right.right = new Node();
                       head.right.right.val =val;
                   } 
                   else {
                       if(head.right.left!=null){
                           head = head.right;
                           continue;
                       }
                       head.right.left = new Node();
                       head.right.left.val =val;
                       head.right.left.ht = head.right.ht-1;
                   }
               }// outer if
               else{ // this is the case where we needed to insert to make avl but now we are violating
                   if(val<head.right.right.val){
                       if(head.right.right.left != null){
                           head=head.right;
                           continue;
                       }
                       head.right.right.left = new Node();
                       head.right.right.left.val =val;
                       head.right.right.left.ht =head.right.left.ht-1;
                       rightLeft(head);
                       return root;
                   }
                   else{
                       if(head.right.right.right !=null){
                           head = head.right;
                           continue;
                       }
                       head.right.right.right = new Node();
                       head.right.right.right.val = val;
                       head.right.right.right.ht =head.right.right.ht-1;
                       rightRight(head);
                       return root;
                   }                 
               }
           }
       } // outer if
   }
   // we are now at the leaf and should add the Node
  

  
}
static void leftLeft(Node head){
	Node temp = new Node(head.left.val,head.left.ht,head.left.left,head.left.right);
	temp.left = head.left.left.right;
    head.left = head.left.left;
    head.left.right = temp;
    
    
     
}
static void leftRight(Node head){
	Node temp = new Node(head.left.left.val,head.left.left.ht,head.left.left.left,head.left.left.right);
    temp.right = head.left.right.left;
    head.left = head.left.right;
    head.left.left= temp;
    leftLeft(head);
}
static void rightRight(Node head){
	Node temp = new Node(head.right.val,head.right.ht,head.right.left,head.right.right);
	temp.right = head.right.right.left;
    head.right = head.right.right;
    head.right.left = temp;
 // now we correct the heights
    head.right.ht = head.right.ht+1;
    head.right.left.ht = head.right.left.ht-1;
    head.right.right.ht = head.right.left.ht;
    
     
}
static void rightLeft(Node head){
	Node temp = new Node(head.right.right.val,head.right.right.ht,head.right.right.left,head.right.right.right);
    temp.left = head.right.left.right;
    head.right = head.right.left;
    head.right.right= temp;
    /// heights
    head.right.right.ht = head.right.right.ht+1;
    head.right.right.right.ht = head.right.right.ht+1;
    rightRight(head);
}
static int balanceFactor(Node x){
	int l;
	int r;
	if(x.left == null) l = 0;
	else l = x.left.ht;
	if(x.right ==null) r = 0;
	else r = x.right.ht;
	return l-r;
}
static void printTree(Node root){
	LinkedList<Node> queue = new LinkedList<Node>();
	queue.add(root);
	while(!queue.isEmpty()){
		Node head = queue.removeLast();
		System.out.println(head.val + "balance factor" + balanceFactor(head));
		if(head.right!=null) queue.add(head.right);
		if(head.left!=null) queue.add(head.left);
	}
}
}