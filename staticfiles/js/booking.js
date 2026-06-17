
    <script>
        document.getElementById("ticketForm").addEventListener("submit", function(event) {
            event.preventDefault();
            
            const fromCity = document.getElementById("fromCity").value;
            const toCity = document.getElementById("toCity").value;
            const travelDate = document.getElementById("travelDate").value;
            const travelTime = document.getElementById("travelTime").value;
            const seatNumber = document.getElementById("seatNumber").value;
            const passengerName = document.getElementById("passengerName").value;

            const bookingCard = `
                <div class="booking-card">
                    <div class="booking-details">
                        <h4>${fromCity} → ${toCity}</h4>
                        <p><strong>Date:</strong> ${travelDate}</p>
                        <p><strong>Time:</strong> ${travelTime}</p>
                        <p><strong>Seat No:</strong> ${seatNumber}</p>
                        <p><strong>Passenger:</strong> ${passengerName}</p>
                        <p><strong>Status:</strong> <span class="confirmed">Confirmed</span></p>
                    </div>
                    <div class="booking-actions">
                        <button class="btn btn-success"><i class="bi bi-printer"></i> Print</button>
                        <button class="btn btn-primary"><i class="bi bi-cloud-download"></i> Download</button>
                        <button class="btn btn-danger" onclick="this.parentElement.parentElement.remove()">
                            <i class="bi bi-x-circle"></i> Cancel
                        </button>
                    </div>
                </div>
            `;

            document.getElementById("bookingList").innerHTML += bookingCard;

            document.getElementById("ticketForm").reset();
        });
    </script>
