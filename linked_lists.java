/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
class Node {
     int data;
     Node next;
 }   

Node InsertNth(Node head, int data, int position) {
   // This is a "method-only" submission. 
    // You only need to complete this method. 
    if(head == null){
        Node temp = new Node();
        temp.data = data;
        temp.next=null;
        return temp;
    }
    if(position == 0){
        Node temp = new Node();
        temp.data = data;
        temp.next=head;
        return temp;
    }
    Node temp = new Node();
    temp.data = data;
    Node start = head;
    for(int i = 0;i < position-1;i++){ // point to node prior to position
        head = head.next;
    }
    Node afterInsert = head.next;
    head.next = temp;
    if(afterInsert!= null) temp.next = afterInsert;
    else temp.next= null;
    
    return start;
}
void ReversePrint(Node head) {
	  // This is a "method-only" submission. 
	  // You only need to complete this method. 
	    if(head==null) return;
	    if(head.next==null){
	        System.out.println(head.data);
	        return;
	    }
	    ReversePrint(head.next);
	    System.out.println(head.data);
	    
	}
/*
Reverse a linked list and return pointer to the head
The input list will have at least one element  
Node is defined as  
class Node {
   int data;
   Node next;
}
*/
  // This is a "method-only" submission. 
  // You only need to complete this method. 
Node Reverse(Node head) {
  if(head.next==null) return head;
  else{
  	Node temp = head.next;
  	head.next = null;
      return Rec_Reverse(head,temp);
  }
     
}
Node Rec_Reverse(Node head,Node saved_ptr){
  if(saved_ptr.next==null){
      saved_ptr.next= head;
      return saved_ptr;
  }
      
  
  Node temp = saved_ptr.next;
  saved_ptr.next = head;
  Node x= Rec_Reverse(saved_ptr,temp);
  return x;
  
}
/*
Compare two linked lists A and B
Return 1 if they are identical and 0 if they are not. 
Node is defined as 
class Node {
   int data;
   Node next;
}
*/
int CompareLists(Node headA, Node headB) {
  // This is a "method-only" submission. 
  // You only need to complete this method 
  if(headA==null && headB==null) return 1;
  else if(headA==null) return 0;
  else if(headB==null) return 0;   
  else{
      while(headA!=null && headB!=null){
          if(headA.data != headB.data) return 0;
          headA = headA.next;
          headB = headB.next;
          if(headA == null && headB!=null) return 0;
          if(headB == null && headA!=null) return 0;        
      }
      if(headA == null && headB!=null) return 0;
      if(headB == null && headA!=null) return 0;
      if((headA==null && headB==null) || headA.data == headB.data) return 1;
      else return 0;
  }      
}
/*
Merge two linked lists 
head pointer input could be NULL as well for empty list
Node is defined as 
class Node {
   int data;
   Node next;
}
*/

Node MergeLists(Node headA, Node headB) {
   // This is a "method-only" submission. 
   // You only need to complete this method 
  
  if(headA==null && headB==null) return null;
  else if(headA==null) return headB;
  else if(headB==null) return headA;
  else{
      Node start = headA;
      if(headA.data <=headB.data)start = headA;
      else start = headB;
      Node currentA = headA;
      Node currentB = headB;
      
      while(currentA != null && currentB != null){
          if(currentA.data <= currentB.data){ // either we move forward or add an element from list B
          
              if(currentA.next == null){
                  currentA.next= currentB;
                  return start;
              }//if2
              if(currentA.next.data > currentB.data) 
              {
                  if(currentB.next==null){
                      currentB.next=currentA.next;
                      currentA.next= currentB;
                      return start;
                  }
                  Node temp = currentB.next;
                  currentB.next = currentA.next;
                  currentA.next = currentB;
                  currentB = temp;
              }
              else
                  {
                  if(currentA.next==null) return start;
                  else currentA=currentA.next;
              }
          }// outer if
           else if(currentA.data > currentB.data){ // either we move forward or add an element from list B
               if(currentB.next == null){
                   currentB.next=currentA;
                   return start;
               }
              if(currentB.next.data > currentA.data) {
                  if(currentA.next==null){
                      currentA.next=currentB.next;
                      currentB.next= currentA;
                      return start;
                  }
                  Node temp = currentA.next;
                  currentA.next = currentB.next;
                  currentB.next = currentA;
                  currentA = temp;
              }
              
               else
                   {
                   if(currentB.next==null) return start;
                   else currentB=currentB.next;
                     }
              }

          
      }// else
      return start;
      
  }
}
/*
Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/

Node RemoveDuplicates(Node head) {
  // This is a "method-only" submission. 
  // You only need to complete this method. 
    Node prev_node = null;
    Node start = head;
    while(head.next!=null){
        Node next_node = head.next;
        if(head.data == next_node.data) {
            if(next_node.next == null) head.next= null;
            else{// duplicate found, must find first different value
                Node sentinel = next_node;
                while(sentinel.next!=null){
                    if(sentinel.next.data!=head.data){
                        head.next = sentinel.next;
                        break;
                    } 
                    sentinel=sentinel.next;
                }  
                if(sentinel.next==null){
                    head.next= null;
                    return start;
                }
            }           
        }
    
        head = head.next;        
    }
    return start;

}
/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

A Node is defined as: 
    class Node {
        int data;
        Node next;
    }
*/

boolean hasCycle(Node head) {
    HashSet<Node> visited = new HashSet<Node>();
    if(head==null || head.next == null) return false;
    visited.add(head);
    while(head.next!=null){
        if(visited.contains(head.next)) return true;
        visited.add(head.next);
        head = head.next;
    }
    return false;
}
/*
Insert Node at the end of a linked list 
head pointer input could be NULL as well for empty list
Node is defined as 
class Node {
   int data;
   Node next;
}
*/
int FindMergeNode(Node headA, Node headB) { // increment each list 1 at a time because of potential cycles
  HashSet<Node> visited = new HashSet<Node>();
  visited.add(headA);
  if(visited.contains(headB)) return headB.data;
  visited.add(headB);
  headA = headA.next;
  headB= headB.next;    
  int count = 1;
  while(true){
      if(headA == null && headB== null) return -1;
      if(count % 2 == 0){
          if(headB==null){
              count++;
              continue;
          }
          if(visited.contains(headB)){
              return headB.data;
          } 
          visited.add(headB);
          headB= headB.next;
      }
      if(count % 2 != 0){
          if(headA==null){
              count++;continue;
          }
          if(visited.contains(headA)){
              return headA.data;
          } 
          visited.add(headA);
          headA = headA.next;
      }
      count++;
  }      
}
/*
Insert Node at the end of a linked list 
head pointer input could be NULL as well for empty list
Node is defined as 
class Node {
   int data;
   Node next;
   Node prev;
}
*/

Node SortedInsert(Node head,int data) {
  Node temp = new Node();
  temp.data = data;
  // find the correct location to insert
  if(head.next == null){
      head.next=temp;
      return head;
  }
  Node start = head;
  int inserted = -1;
  while(head.next!=null){
      if(head.next.data > data){
          Node afterInsert = head.next;
          head.next = temp;
          temp.next = afterInsert;
          temp.prev = head;
          afterInsert.prev = temp;
          inserted = 1;           
      }
      head = head.next;
  }
  if(inserted == -1) head.next=temp;
  return start;
}
/*
Insert Node at the end of a linked list 
head pointer input could be NULL as well for empty list
Node is defined as 
class Node {
   int data;
   Node next;
   Node prev;
}
*/
Node Reverse(Node head) {
  if(head==null) return null;
  Node prev_node = null;
  if(head.next == null){
      return head;
  }
  Node next_node = head.next;
  while(head!=null){
      if(head.next==null){
          head.next = prev_node;
          head.prev = null;
          return head;
      }
      head.next = prev_node;
      head.prev = next_node;
      head = next_node;
      prev_node = head.prev;
      next_node = head.next;
  }
  return head;  
}






	