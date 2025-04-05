import { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";

export default function App() {
  const [noiseLevel, setNoiseLevel] = useState(0);
  const [isLoud, setIsLoud] = useState(false);
  const threshold = 60; // Adjust for sensitivity

  const audioContextRef = useRef(null);
  const analyserRef = useRef(null);
  const dataArrayRef = useRef(null);
  const sourceRef = useRef(null);

  useEffect(() => {
    async function initAudio() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        audioContextRef.current = new (window.AudioContext || window.webkitAudioContext)();
        analyserRef.current = audioContextRef.current.createAnalyser();
        sourceRef.current = audioContextRef.current.createMediaStreamSource(stream);
        sourceRef.current.connect(analyserRef.current);
        analyserRef.current.fftSize = 256;

        const bufferLength = analyserRef.current.frequencyBinCount;
        dataArrayRef.current = new Uint8Array(bufferLength);

        const update = () => {
          analyserRef.current.getByteFrequencyData(dataArrayRef.current);
          const values = dataArrayRef.current.reduce((a, b) => a + b, 0);
          const average = values / bufferLength;

          const dbApprox = Math.round((average / 255) * 100); // Approximate dB
          setNoiseLevel(dbApprox);
          setIsLoud(dbApprox > threshold);

          requestAnimationFrame(update);
        };

        update();
      } catch (err) {
        console.error("Microphone access denied or error:", err);
      }
    }

    initAudio();
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-6 space-y-6">
      <h1 className="text-4xl font-bold mb-4">Noise Pollution Monitor</h1>

      <div className="bg-gray-800 w-full max-w-md shadow-xl rounded-2xl p-6 flex flex-col items-center space-y-4">
        <div className="text-2xl">Current Noise Level</div>
        <div className="text-6xl font-mono">{noiseLevel} dB</div>

        <motion.div
          animate={
            isLoud
              ? {
                  opacity: [1, 0.2, 1],
                  scale: [1, 1.2, 1],
                }
              : { opacity: 1, scale: 1 }
          }
          transition={isLoud ? { repeat: Infinity, duration: 0.6 } : {}}
          className={`w-20 h-20 rounded-full ${
            isLoud ? "bg-red-500" : "bg-green-500"
          } shadow-lg`}
        ></motion.div>

        <div className="text-sm text-gray-400">
          {isLoud ? "High noise detected!" : "Noise is within safe limits."}
        </div>
      </div>
    </div>
  );
}
