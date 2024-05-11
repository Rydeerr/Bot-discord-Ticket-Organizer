<h1>Ticket Bot</h1>
    <h2>Description</h2>
    <p>This is a bot to manage support tickets on Discord servers. It allows members to open tickets to report issues or request support, and moderators can mark the tickets as resolved.</p>

<h2>Features</h2>
    <ul>
        <li>Opening support tickets with detailed information.</li>
        <li>Marking tickets as resolved by moderators.</li>
        <li>Integration with an interactive user interface for a better user experience.</li>
    </ul>

<h2>Usage Instructions</h2>

  <ol>
        <li><strong>Bot Setup:</strong>
            <ul>
                <li>Clone this repository to your local machine.</li>
                <li>Ensure you have Python installed.</li>
                <li>Install the required dependencies with <code>pip install -r requirements.txt</code>.</li>
                <li>Replace <code>"YOUR_TOKEN"</code> in the code with your Discord bot token.</li>
            </ul>
        </li>
        <li><strong>Running the Bot:</strong>
            <ul>
                <li>Execute the <code>bot.py</code> file.</li>
            </ul>
        </li>
        <li><strong>Available Commands:</strong>
            <ul>
                <li><code>/ticket</code>: Opens a new support ticket.</li>
                <li>Parameters:
                    <ul>
                        <li><code>ticket</code>: Description of the problem.</li>
                        <li><code>product</code>: Related product.</li>
                        <li><code>purchase</code>: Purchase ID.</li>
                        <li><code>email</code>: Associated email.</li>
                        <li><code>reason</code>: Reason for the ticket.</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ol>
</body>
</html>
