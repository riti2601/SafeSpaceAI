export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 flex flex-col items-center justify-center p-6">
      <h1 className="text-4xl font-bold text-gray-800 mb-4">SafeSpace AI</h1>
      <p className="text-lg text-gray-600 mb-6 text-center max-w-lg">
        Your free AI companion for mental well-being. Talk to an empathetic AI therapist anytime, anywhere.
      </p>
      <div className="flex gap-4">
        <a href="/chat" className="px-6 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700">Start Chatting</a>
        <a href="/about" className="px-6 py-3 bg-gray-200 text-gray-800 rounded-lg shadow hover:bg-gray-300">Learn More</a>
      </div>
    </main>
  );
}
