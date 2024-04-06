class Node {
	constructor(data, pointer) {
		this.data = data; //data or value
		this.pointer = pointer || null; //pointer
	}
}

//init the link list
class LinkList {
	constructor(data) {
		this.head = null;
		this.size = 0;
	}
	push(data) {
		//setting head with one Node class
		this.head = new Node(data , this.head);
		this.size++;
	}

	//search
	//search (First iteratively then recursively)
	searchIteratively(data) {
		let current = this.head;
		while(current){
			if (current.data === data){
				return current;
			}
			else {
				current = current.pointer;
			}
		}
	}
	// chatgpt random code 
	// searchRecursively(target, current = this.head) {
	// 	if (current === null) {
	// 		return false; // Reached end of the list, target not found
	// 	}
	// 	if (current.data === target) {
	// 		return true; // Found the target
	// 	}
	// 	return this.searchRecursively(target, current.pointer); // Move to the next node recursively
	// }
	
	searchRecursively(data , current = this.head) {
		// console.log(this.head); prints the current head Node
		if (current.pointer === null) {
			return false;
		}
		if (current.data === data) {
			return current;
		}
		return this.searchRecursively(data, current.pointer);


	}
	// To delete a node from linked list, we need to do following steps.
	// 1) Find previous node of the node to be deleted.
	// 2) Change the next of previous node.
	// 3) Free memory for the node to be deleted.
	delete(data) {

	}

	//print
	print(){
		let current = this.head;
		while(current){
			console.log(current.data)
			current = current.pointer;
		}

	}

	// //print backwards
	// printBackwards() {

	// }
}


let ll = new LinkList();
ll.push(5);
ll.push(10);
ll.push(20);

// console.log(ll.searchIteratively(10))//10

// ll.print(); //20, 10, 5
console.log(ll.searchRecursively(10)); //10

ll.delete(10); //20, 5