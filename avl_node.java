package artificial;


class avl_node 
   int val;   //Value
   int ht;      //Height
   avl_node left;   //Left child
   avl_node right;   //Right child



static avl_node insert(avl_node root,int val)
{
   avl_node head = root;
   int prev_head_balance = head.left.ht-head.right.ht;
   while(Something){
       // code the cases where we do not disrupt avl first
       if(val < head.left.val){
           if(head.left == null){ // we are able to insert without disrupting avl
               head.left.val = val;
               head.left.ht = head.ht-1;
           }
           else{ // we are not able to insert without disrupting avl unless bf was 0
               if(prev_head_balance == 0){
                   if(val < head.left.val){
                       if(head.left.left!=null){
                           head = head.left;
                           continue;
                       }
                       head.left.left.val =val;
                   } 
                   else {
                       if(head.left.right!=null){
                           head = head.left;
                           continue;
                       }
                       head.left.right.val =val;
               }
               else{ // this is the case where we needed to insert to make avl but now we are violating
                   if(val<head.left.left.val){
                       if(head.left.left.left != null){
                           head=head.left;
                           continue;
                       }
                       head.left.left.left.val =val;
                       leftLeft(head);
                   }
                   else{
                       if(head.left.left.right !=null){
                           head = head.left;
                           continue;
                       }
                       head.left.left.right.val = val;
                       leftRight(head.left);
                   } 
                   
                   
               }
           }
       } // outer if
       
   }
   // we are now at the leaf and should add the avl_node
  
}
static avl_node leftLeft(avl_node head){
    
     head.left.left.left = head.left;
     head.left = head.left.left;  
}
static avl_node leftRight(avl_node head){
    head.left.left;
}