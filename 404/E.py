import sys

class InputHandler:
    def __init__(self, mode="Console", file_path="input.txt"):
        self.mode = mode
        self.file_path = file_path
        self.N = 0
        self.C = []
        self.A = []
        self.lines = []
        self.G = []
        self.P = []
        self.F = []
        self.M = []
        self.Answer = 0

    def get_input_lines(self):
        if self.mode == "Console":
            return self._read_from_console()
        elif self.mode == "File":
            return self._read_from_file()
        else:
            raise ValueError("Invalid mode. Use 'Console' or 'File'.")

    def _read_from_console(self):
        lines = []
        try:
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
        except EOFError:
            pass
        return lines

    def _read_from_file(self):
        with open(self.file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def parse_input(self):
        self.lines = self.get_input_lines()
       
        if self.lines:
            self.N = int(self.lines[0])
            self.C = [0] + list(map(int, self.lines[1].split()))
            self.A = [0] + list(map(int, self.lines[2].split()))

        self.G = [[] for i in range(0, self.N)]
        self.P = [[] for i in range(0, self.N)]
        self.F = [sys.maxsize for i in range(0, self.N)]

    def solve(self):
        self.parse_input()

        # Build graph
        for i in range(1, self.N):
            for c in range (1, self.C[i] + 1):
                self.G[i-c].append(i)

        # Build fastest routes and parent map
        self.F[0] = 0
        for i in range(0, self.N - 1):
            for v in self.G[i]:
                if (self.F[i] + 1 < self.F[v]):
                    self.F[v] = self.F[i] + 1
                    self.P[v] = i
                elif (self.F[i] + 1 == self.F[v]):
                    if self.A[i] > self.A[self.P[v]]:
                        self.F[v] = self.F[i] + 1
                        self.P[v] = i

        
        # Move the beans from furthest to closest
        mx = max(self.F)
        for step in range(mx, 0, -1):
            # Create a list of with distance of step
            self.M = []
            for i in range(1, self.N):
                if self.F[i] == step:
                    self.M.append(i)

            # Move bean 1 step from bowl in M
            for bowl in self.M:
                if self.A[bowl] > 0:
                    self.A[self.P[bowl]] += self.A[bowl]
                    self.A[bowl] = 0
                    self.Answer += 1
        
        print(self.Answer)

def main():
    # Instantiate the class with mode: "Console" or "File"
    #handler = InputHandler("Console")
    handler = InputHandler("File", "E_input1.txt")
    
    # Call the solve method
    handler.solve()

# Standard Python entry point
if __name__ == "__main__":
    main()