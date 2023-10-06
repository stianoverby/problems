import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Teque {

    private class Deque {
        private int[] array;
        private int size;
        private int front;
        private int rear;

        public Deque(int capcaity){
            array = new int[capcaity];
            size = 0;
            front = 0;
            rear = 0;
        }

        public void add_front(int item){
            if (isFull()){
                throw new IllegalStateException("Deque is full");
            }
            front = (front - 1 + array.length) % array.length;
            array[front] = item;
            size++;
   
        }

        public void add_back(int item) {
            if (isFull()){
                throw new IllegalStateException("Deque is full");
            }
            array[rear] = item;
            rear = (rear + 1) % array.length;
            size++;
        }

        public int remove_front() {
            if (isEmpty()){
                throw new IllegalStateException("Deque empty");
            }
            int item = array[front];
            front = (front + 1) % array.length;
            size--;
            return item;
        }
    
        public int remove_back() {
            if (isEmpty()){
                throw new IllegalStateException("Deque empty");
            }
            rear = (rear - 1 + array.length) % array.length;
            int item = array[rear];
            size--;
            return item;
        }

        public int get(int index) {
            if (index < 0 || index >= size){
                throw new IndexOutOfBoundsException("Index i out of bounds");
            }
            int conceptualIndex = (front + index) % array.length;
            return array[conceptualIndex];
        }

        public boolean isEmpty() {
            return size == 0;
        }
    
        public boolean isFull() {
            return size == array.length;
        }
    
        public int size() {
            return size;
        }
    
    }
    Deque front = new Deque(500001);
    Deque back = new Deque(500001);

    void push_back(int i){
        back.add_back(i);
        balance();
    }

    void push_front(int i){
        front.add_front(i);
        balance();
    }

    void push_middle(int i){
        front.add_back(i);
        balance();
    }

    Integer get(int index){
        if(index < front.size()){
            return front.get(index);
        }
        return back.get(index - front.size());
    }

    private void balance() {
        /* Move from front to back */
        while (front.size() > back.size() + 1) {
            back.add_front(front.remove_back());
        }

        /* Move from back to front */
        while (back.size() > front.size()) {
            front.add_back(back.remove_front());
        }
    }

    public static void main(String[] args){

        Teque dataStructure = new Teque();
        StringBuilder output = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
            int n = Integer.parseInt(br.readLine());
            
            for (int i = 0; i < n; i++) {
                String line = br.readLine();
                String[] parts = line.split(" ");
                String operation = parts[0];
                
                switch (operation) {
                    case "push_back":
                        int x = Integer.parseInt(parts[1]);
                        dataStructure.push_back(x);
                        break;
                        
                    case "push_front":
                        int y = Integer.parseInt(parts[1]);
                        dataStructure.push_front(y);
                        break;
                        
                    case "push_middle":
                        int z = Integer.parseInt(parts[1]);
                        dataStructure.push_middle(z);
                        break;
                        
                    case "get":
                        int index = Integer.parseInt(parts[1]);
                        output.append(dataStructure.get(index)).append("\n");
                        break;
                }
            }
            writer.write(output.toString());
            writer.flush();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}

