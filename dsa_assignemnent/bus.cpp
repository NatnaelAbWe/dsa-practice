#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

// ------------------- Customer -------------------
struct Customer {
    string name, mobile, email, city;
    int age;
};

// ------------------- Bus -------------------
struct Bus {
    string busNumber, start, end, startTime;
    int totalSeats, fare;
    int reservedSeats = 0;
    queue<int> waitlist; // store indices of waiting customers
};

// ------------------- Reservation System -------------------
class BusReservationSystem {
private:
    vector<Customer> customers;
    vector<Bus> buses;

public:
    stack<int> customerStack; // for newest → oldest view

    // --- Customer Operations ---
    void registerCustomer() {
        Customer c;
        cin.ignore();
        cout << "Name: "; getline(cin, c.name);
        cout << "Mobile: "; getline(cin, c.mobile);
        cout << "Email: "; getline(cin, c.email);
        cout << "City: "; getline(cin, c.city);
        cout << "Age: "; cin >> c.age;
        customers.push_back(c);
        customerStack.push(customers.size() - 1);
        cout << "Customer registered successfully.\n";
    }

    void displayCustomersOldest() {
        cout << "\n-- Customers (Oldest → Newest) --\n";
        for(auto &c : customers) {
            cout << c.name << " | " << c.mobile << " | " << c.email << " | " << c.city << " | " << c.age << "\n";
        }
    }

    void displayCustomersNewest() {
        cout << "\n-- Customers (Newest → Oldest) --\n";
        stack<int> tempStack = customerStack;
        while(!tempStack.empty()) {
            int idx = tempStack.top(); tempStack.pop();
            Customer &c = customers[idx];
            cout << c.name << " | " << c.mobile << " | " << c.email << " | " << c.city << " | " << c.age << "\n";
        }
    }

    // --- Bus Operations ---
    void registerBus() {
        Bus b;
        cin.ignore();
        cout << "Bus Number: "; getline(cin, b.busNumber);
        cout << "Start Point: "; getline(cin, b.start);
        cout << "End Point: "; getline(cin, b.end);
        cout << "Start Time: "; getline(cin, b.startTime);
        cout << "Total Seats: "; cin >> b.totalSeats;
        cout << "Fare: "; cin >> b.fare;
        buses.push_back(b);
        cout << "Bus registered successfully.\n";
    }

    void displayBuses() {
        cout << "\n-- Available Buses --\n";
        for(size_t i=0;i<buses.size();i++){
            Bus &b = buses[i];
            cout << i << ". " << b.busNumber << " | " << b.start << " -> " << b.end
                 << " | Seats: " << b.reservedSeats << "/" << b.totalSeats
                 << " | Fare: " << b.fare << " | Time: " << b.startTime << "\n";
        }
    }

    void reserveSeat() {
        displayCustomersOldest();
        int custIdx; cout << "Select customer index: "; cin >> custIdx;
        displayBuses();
        int busIdx; cout << "Select bus index: "; cin >> busIdx;

        if(busIdx < 0 || busIdx >= buses.size() || custIdx < 0 || custIdx >= customers.size()){
            cout << "Invalid index!\n"; return;
        }

        Bus &b = buses[busIdx];
        if(b.reservedSeats < b.totalSeats){
            b.reservedSeats++;
            cout << "Seat reserved for " << customers[custIdx].name << ". Notification sent!\n";
        } else {
            b.waitlist.push(custIdx);
            cout << "Bus full! Added to waitlist. You will be notified when seat is free.\n";
        }
    }

    void cancelReservation() {
        displayBuses();
        int busIdx; cout << "Select bus to cancel seat: "; cin >> busIdx;
        if(busIdx < 0 || busIdx >= buses.size()){ cout << "Invalid bus index!\n"; return; }

        Bus &b = buses[busIdx];
        if(b.reservedSeats > 0){
            b.reservedSeats--;
            cout << "Reservation cancelled. Notification sent.\n";
            if(!b.waitlist.empty()){
                int custIdx = b.waitlist.front(); b.waitlist.pop();
                b.reservedSeats++;
                cout << "Seat assigned to next in waitlist: " << customers[custIdx].name << ". Notification sent!\n";
            }
        } else {
            cout << "No reservations to cancel.\n";
        }
    }
};

// ------------------- Main -------------------
int main(){
    BusReservationSystem system;
    int choice;
    do {
        cout << "\n--- Bus Reservation System ---\n";
        cout << "1. Register Customer\n2. Register Bus\n3. Display Customers Oldest\n4. Display Customers Newest\n";
        cout << "5. Display Buses\n6. Reserve Seat\n7. Cancel Reservation\n0. Exit\n";
        cout << "Enter choice: "; cin >> choice;

        switch(choice){
            case 1: system.registerCustomer(); break;
            case 2: system.registerBus(); break;
            case 3: system.displayCustomersOldest(); break;
            case 4: system.displayCustomersNewest(); break;
            case 5: system.displayBuses(); break;
            case 6: system.reserveSeat(); break;
            case 7: system.cancelReservation(); break;
            case 0: cout << "Exiting...\n"; break;
            default: cout << "Invalid choice.\n";
        }
    } while(choice != 0);
}
