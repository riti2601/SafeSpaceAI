export default function About() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 flex flex-col items-center justify-center p-6">
      <h1 className="text-3xl font-bold text-gray-800 mb-4">About SafeSpace AI</h1>
      <p className="text-lg text-gray-600 max-w-2xl text-center">
        SafeSpace AI is a free platform where anyone can chat with an AI trained on the best therapeutic practices. 
        We are not a replacement for professional therapy, but we aim to provide support for those who cannot afford or access one. 
        Your conversations are private, and we include safeguards such as trigger warnings for harmful content.
      </p>
    </main>
  );
}
