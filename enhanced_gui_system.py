#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Enhanced GUI System
Steam-ready enhanced interface with graphics and polish
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
from pathlib import Path
from PIL import Image, ImageTk
import threading
import queue

# Import existing game components
try:
    from gui import CaveGameGUI as BaseGUI
    from game_refactored import play_game
    from game_events import start_game
    from ui import title_screen
except ImportError as e:
    print(f"⚠️ Import error: {e}")
    print("Make sure you're running from the project root directory")
    sys.exit(1)

class EnhancedGameGUI(BaseGUI):
    """Enhanced GUI with graphics, animations, and Steam features"""
    
    def __init__(self, root=None):
        # Initialize graphics system first
        self.graphics_loaded = False
        self.character_sprites = {}
        self.background_images = {}
        self.sound_enabled = True
        
        # Store root if provided, otherwise let base class create it
        self._external_root = root
        
        # Initialize base GUI
        super().__init__()
        
        # If external root was provided, use it instead of the one created by base class
        if self._external_root:
            if hasattr(self, 'root') and self.root != self._external_root:
                self.root.destroy()  # Clean up the auto-created root
            self.root = self._external_root
        
        # Load enhanced features
        self.setup_graphics()
        self.setup_steam_features()
        
    def setup_window(self):
        """Enhanced window setup with better scaling and Steam overlay support"""
        self.root.title("🗻 SHABUYA Cave Adventure")
        
        # Better default size for Steam
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        self.root.configure(bg='#1a0f08')
        
        # Steam overlay compatibility
        self.root.attributes('-topmost', False)
        
        # Better DPI awareness
        try:
            self.root.tk.call('tk', 'scaling', 2.0 if self.get_high_dpi() else 1.0)
        except:
            pass
        
        # Center on screen
        self.center_window()
        
        # Enhanced icon
        self.set_window_icon()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def get_high_dpi(self) -> bool:
        """Detect high DPI displays"""
        try:
            import tkinter as tk
            root = tk.Tk()
            root.withdraw()
            dpi = root.winfo_fpixels('1i')
            root.destroy()
            return dpi > 100
        except:
            return False
    
    def set_window_icon(self):
        """Set enhanced window icon"""
        try:
            icon_path = Path("game_assets/icons/shabuya_icon.png")
            if icon_path.exists():
                # Use as window icon for tkinter
                try:
                    self.root.iconbitmap(str(icon_path))
                except:
                    pass  # Icon setting is optional
        except Exception as e:
            print(f"Could not load window icon: {e}")
    
    def setup_graphics(self):
        """Initialize enhanced graphics system"""
        try:
            self.load_character_sprites()
            self.load_background_images()
            self.setup_animations()
            self.graphics_loaded = True
            print("✅ Graphics system initialized")
        except Exception as e:
            print(f"⚠️ Graphics initialization warning: {e}")
            self.graphics_loaded = False
    
    def load_character_sprites(self):
        """Load character class sprites"""
        sprite_dir = Path("game_assets/sprites")
        if not sprite_dir.exists():
            sprite_dir.mkdir(parents=True, exist_ok=True)
            self.create_default_sprites(sprite_dir)
        
        sprite_files = {
            # Player character sprites
            'warrior': 'warrior_sprite.png',
            'rogue': 'rogue_sprite.png', 
            'mage': 'mage_sprite.png',
            # Enemy sprites (specific types only)
            'primitive_creature': 'primitive_creature_sprite.png',
            'divine_heart': 'divine_heart_sprite.png',
            'cave_guardian': 'cave_guardian_sprite.png'
        }
        
        for sprite_name, filename in sprite_files.items():
            sprite_path = sprite_dir / filename
            if sprite_path.exists():
                try:
                    img = Image.open(sprite_path)
                    img = img.resize((64, 64), Image.Resampling.LANCZOS)
                    self.character_sprites[sprite_name] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Could not load sprite {sprite_name}: {e}")
    
    def create_default_sprites(self, sprite_dir: Path):
        """Create simple default sprites if none exist"""
        try:
            from PIL import Image, ImageDraw
            
            sprite_configs = {
                # Player characters
                'warrior': {'color': '#8B4513', 'symbol': '🛡️'},
                'rogue': {'color': '#2F4F2F', 'symbol': '🗡️'},
                'mage': {'color': '#4B0082', 'symbol': '🔮'},
                # Enemy sprites (specific types only)
                'primitive_creature': {'color': '#A0522D', 'symbol': '🦎'},
                'divine_heart': {'color': '#4B0082', 'symbol': '💜'},
                'cave_guardian': {'color': '#696969', 'symbol': '🗿'}
            }
            
            for name, config in sprite_configs.items():
                # Create simple colored square with emoji
                img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
                draw = ImageDraw.Draw(img)
                
                # Background circle
                draw.ellipse([8, 8, 56, 56], fill=config['color'])
                
                img.save(sprite_dir / f"{name}_sprite.png")
            
            print("✅ Default sprites created")
            
        except ImportError:
            print("⚠️ PIL not available - sprites will be text-only")
    
    def load_background_images(self):
        """Load scene background images"""
        bg_dir = Path("game_assets/backgrounds")
        if not bg_dir.exists():
            bg_dir.mkdir(parents=True, exist_ok=True)
        
        background_files = {
            # Current backgrounds
            'cave_entrance': 'cave_entrance.png',
            'skull_chamber': 'skull_chamber.png',
            'primitive_village': 'primitive_village.png',
            'menu': 'menu.png',
            # Missing backgrounds (will get placeholders)
            'alley': 'alley.png',
            'armory': 'armory.png',
            'chief_house': 'chief_house.png',
            'healing_pool': 'healing_pool.png',
            'village_changed': 'village_changed.png'
        }
        
        # Check for missing backgrounds and create them
        missing_backgrounds = []
        for bg_name, filename in background_files.items():
            bg_path = bg_dir / filename
            if not bg_path.exists():
                missing_backgrounds.append(bg_name)
        
        if missing_backgrounds:
            self.create_missing_backgrounds(bg_dir, missing_backgrounds)
        
        # Load all backgrounds
        for bg_name, filename in background_files.items():
            bg_path = bg_dir / filename
            if bg_path.exists():
                try:
                    img = Image.open(bg_path)
                    # Resize to fit game panel
                    img = img.resize((400, 300), Image.Resampling.LANCZOS)
                    self.background_images[bg_name] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Could not load background {bg_name}: {e}")
            else:
                print(f"Background file missing: {filename}")
    
    def create_missing_backgrounds(self, bg_dir: Path, missing_list):
        """Create placeholder backgrounds for missing scenes"""
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            bg_configs = {
                # Current backgrounds
                'cave_entrance': [(20, 10, 5), (60, 40, 20)],  # Brown gradient
                'skull_chamber': [(40, 20, 20), (20, 10, 10)], # Dark red
                'primitive_village': [(10, 40, 10), (30, 60, 30)], # Green
                'menu': [(10, 10, 20), (30, 20, 40)], # Purple
                # Missing backgrounds (placeholders)
                'alley': [(15, 15, 15), (35, 35, 35)], # Dark grey gradient
                'armory': [(30, 30, 40), (50, 50, 60)], # Blue-grey
                'chief_house': [(40, 25, 10), (60, 45, 30)], # Brown hut
                'healing_pool': [(10, 30, 50), (30, 50, 70)], # Blue healing
                'village_changed': [(25, 15, 35), (45, 35, 55)] # Purple mystical
            }
            
            scene_labels = {
                'alley': 'ALLEY SCENE',
                'armory': 'ARMORY SCENE', 
                'chief_house': 'CHIEF HOUSE',
                'healing_pool': 'HEALING POOL',
                'village_changed': 'VILLAGE CHANGED'
            }
            
            for bg_name in missing_list:
                if bg_name in bg_configs:
                    color1, color2 = bg_configs[bg_name]
                    img = Image.new('RGB', (400, 300))
                    draw = ImageDraw.Draw(img)
                    
                    # Simple vertical gradient
                    for y in range(300):
                        ratio = y / 300
                        r = int(color1[0] * (1-ratio) + color2[0] * ratio)
                        g = int(color1[1] * (1-ratio) + color2[1] * ratio)
                        b = int(color1[2] * (1-ratio) + color2[2] * ratio)
                        draw.line([(0, y), (400, y)], fill=(r, g, b))
                    
                    # Add text label if it's a placeholder
                    if bg_name in scene_labels:
                        try:
                            font = ImageFont.load_default()
                            text = scene_labels[bg_name]
                            bbox = draw.textbbox((0, 0), text, font=font)
                            text_width = bbox[2] - bbox[0]
                            text_height = bbox[3] - bbox[1]
                            x = (400 - text_width) // 2
                            y = (300 - text_height) // 2
                            
                            # Text with outline for visibility
                            for dx in [-1, 0, 1]:
                                for dy in [-1, 0, 1]:
                                    if dx or dy:
                                        draw.text((x+dx, y+dy), text, fill='black', font=font)
                            draw.text((x, y), text, fill='white', font=font)
                        except Exception:
                            # Fallback text
                            fallback_text = scene_labels.get(bg_name, bg_name.upper()) or "PLACEHOLDER"
                            draw.text((150, 140), fallback_text, fill='white')
                    
                    filename = f"{bg_name}.png"
                    img.save(bg_dir / filename)
                    print(f"✅ Created background placeholder: {filename}")
            
        except ImportError:
            print("⚠️ PIL not available - backgrounds will be plain")
    
    def setup_animations(self):
        """Setup simple animations and transitions"""
        self.animation_frame = 0
        self.animation_running = False
        
        # Start animation loop
        self.animate()
    
    def animate(self):
        """Simple animation loop for visual polish"""
        if self.graphics_loaded:
            self.animation_frame = (self.animation_frame + 1) % 60
            
            # Add subtle visual effects here
            # Example: pulsing borders, animated sprites, etc.
        
        # Schedule next frame
        self.root.after(100, self.animate)
    
    def setup_steam_features(self):
        """Initialize Steam integration features"""
        try:
            # Import Steam integration
            from steam_integration.steam_api import get_steam_integration
            self.steam = get_steam_integration()
            
            # Initialize Steam if available
            if self.steam.steam.initialize():
                print("🎮 Steam integration active")
                self.setup_achievements_ui()
            else:
                print("🎮 Steam integration ready (running standalone)")
                
        except ImportError:
            print("⚠️ Steam integration not available")
            self.steam = None
    
    def setup_achievements_ui(self):
        """Add achievement notifications to UI"""
        self.achievement_queue = queue.Queue()
        self.check_achievements()
    
    def check_achievements(self):
        """Check for achievement updates"""
        if self.steam:
            # Check for new achievements
            # This would be called during gameplay events
            pass
        
        # Schedule next check
        self.root.after(5000, self.check_achievements)  # Check every 5 seconds
    
    def create_enhanced_interface(self):
        """Create the enhanced game interface"""
        # Use base interface as foundation
        self.create_interface()
        
        # Add enhanced visual elements
        self.add_graphics_overlay()
        self.add_settings_menu()
        self.add_fullscreen_support()
    
    def add_graphics_overlay(self):
        """Add graphics overlay to existing interface"""
        if not self.graphics_loaded:
            return
        
        # Add character sprite display - but only if we have the character info widget
        try:
            # Find the character info widget and add sprite above it
            if hasattr(self, 'char_info'):
                # Create a frame for the sprite above the character info
                sprite_frame = tk.Frame(self.char_info.master, bg='#2c1810')
                sprite_frame.pack(before=self.char_info, pady=5)
                
                self.character_sprite_label = tk.Label(sprite_frame, bg='#2c1810')
                self.character_sprite_label.pack()
                
                # Set default sprite
                if 'warrior' in self.character_sprites:
                    self.character_sprite_label.config(image=self.character_sprites['warrior'])
            
            # Add background display to game area
            self.add_background_display()
            
        except Exception as e:
            print(f"Could not add graphics overlay: {e}")
    
    def add_background_display(self):
        """Add background image display to the main game area"""
        try:
            # Find the game display area and add background
            if hasattr(self, 'game_display'):
                # Create a canvas for background behind the text
                self.bg_canvas = tk.Canvas(self.game_display.master, 
                                          width=400, height=300, 
                                          bg='#1a0f08', highlightthickness=0)
                self.bg_canvas.pack(before=self.game_display, pady=(0, 10))
                
                # Set default background (menu)
                if 'menu' in self.background_images:
                    self.bg_canvas.create_image(200, 150, 
                                              image=self.background_images['menu'])
                    self.current_background = 'menu'
                else:
                    # Fallback to solid color
                    self.bg_canvas.create_rectangle(0, 0, 400, 300, 
                                                   fill='#2c1810', outline='')
                
        except Exception as e:
            print(f"Could not add background display: {e}")
    
    def update_scene_background(self, scene_name: str):
        """Update background image based on current scene"""
        if not self.graphics_loaded or not hasattr(self, 'bg_canvas'):
            return
        
        # Map scene names to background files
        scene_bg_map = {
            'Cave Entrance': 'cave_entrance',
            'Skull Chamber': 'skull_chamber', 
            'Primitive Village': 'primitive_village',
            'Alley': 'primitive_village',  # Reuse village background
            'Armory': 'cave_entrance',     # Reuse cave background
            'Cave People Chief House': 'primitive_village',
            'Healing Pool': 'cave_entrance'
        }
        
        bg_key = scene_bg_map.get(scene_name, 'menu')
        
        if bg_key in self.background_images and bg_key != getattr(self, 'current_background', None):
            # Clear canvas and set new background
            self.bg_canvas.delete("all")
            self.bg_canvas.create_image(200, 150, 
                                       image=self.background_images[bg_key])
            self.current_background = bg_key
            print(f"🖼️ Background changed to: {bg_key}")
    
    
    def add_settings_menu(self):
        """Add enhanced settings menu"""
        try:
            # Add to existing interface
            settings_frame = tk.Frame(self.root, bg='#2c1810')
            
            # Graphics settings
            gfx_frame = tk.LabelFrame(settings_frame, text="Graphics", 
                                     fg='#DAA520', bg='#2c1810')
            gfx_frame.pack(fill=tk.X, padx=5, pady=5)
            
            # Fullscreen toggle
            self.fullscreen_var = tk.BooleanVar()
            fullscreen_cb = tk.Checkbutton(gfx_frame, text="Fullscreen",
                                         variable=self.fullscreen_var,
                                         command=self.toggle_fullscreen,
                                         fg='#CD853F', bg='#2c1810',
                                         selectcolor='#3c2820')
            fullscreen_cb.pack(anchor=tk.W)
            
            # Sound toggle
            self.sound_var = tk.BooleanVar(value=True)
            sound_cb = tk.Checkbutton(gfx_frame, text="Sound Effects",
                                    variable=self.sound_var,
                                    command=self.toggle_sound,
                                    fg='#CD853F', bg='#2c1810',
                                    selectcolor='#3c2820')
            sound_cb.pack(anchor=tk.W)
            
        except Exception as e:
            print(f"Could not create settings menu: {e}")
    
    def add_fullscreen_support(self):
        """Add fullscreen support"""
        # Bind F11 for fullscreen toggle
        self.root.bind('<F11>', lambda e: self.toggle_fullscreen())
        self.root.bind('<Escape>', lambda e: self.exit_fullscreen())
        
        self.is_fullscreen = False
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes('-fullscreen', self.is_fullscreen)
        
        if self.is_fullscreen:
            # Hide window decorations
            self.root.configure(cursor='none')
        else:
            self.root.configure(cursor='')
    
    def exit_fullscreen(self):
        """Exit fullscreen mode"""
        if self.is_fullscreen:
            self.is_fullscreen = False
            self.root.attributes('-fullscreen', False)
            self.root.configure(cursor='')
    
    def toggle_sound(self):
        """Toggle sound effects"""
        self.sound_enabled = self.sound_var.get()
        # Sound system would be implemented here
        print(f"Sound effects: {'On' if self.sound_enabled else 'Off'}")
    
    def update_character_sprite(self, class_type: str):
        """Update character sprite based on class"""
        if not self.graphics_loaded:
            return
        
        class_sprites = {
            'Warrior': 'warrior',
            'Rogue': 'rogue', 
            'Mage': 'mage'
        }
        
        sprite_key = class_sprites.get(class_type, 'warrior')
        
        try:
            if hasattr(self, 'character_sprite_label') and sprite_key in self.character_sprites:
                self.character_sprite_label.config(image=self.character_sprites[sprite_key])
        except Exception as e:
            print(f"Could not update character sprite: {e}")
    
    def show_achievement_notification(self, achievement_name: str):
        """Show achievement notification popup"""
        if not self.steam:
            return
        
        # Create notification popup
        notification = tk.Toplevel(self.root)
        notification.title("Achievement Unlocked!")
        notification.geometry("300x100")
        notification.configure(bg='#2c1810')
        notification.attributes('-topmost', True)
        
        # Center notification
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 150
        y = self.root.winfo_y() + 50
        notification.geometry(f"300x100+{x}+{y}")
        
        # Achievement content
        tk.Label(notification, text="🏆 Achievement Unlocked!", 
                font=("Arial", 12, "bold"), fg='#DAA520', bg='#2c1810').pack(pady=10)
        
        tk.Label(notification, text=achievement_name, 
                font=("Arial", 10), fg='#CD853F', bg='#2c1810').pack()
        
        # Auto-close after 3 seconds
        notification.after(3000, notification.destroy)
    
    def enhanced_select_class(self, class_type):
        """Enhanced class selection with graphics"""
        # Call original method
        super().select_class(class_type)
        
        # Add enhancements
        self.update_character_sprite(class_type)
        
        # Trigger Steam achievement
        if self.steam:
            self.steam.on_game_start(class_type)
            
            # Show first steps achievement
            if not self.steam.steam.is_achievement_unlocked("FIRST_STEPS"):
                self.show_achievement_notification("First Steps")
    
    def display_text(self, text):
        """Enhanced text display with scene detection"""
        # Call the parent method to display text
        super().display_text(text)
        
        # Check if text contains scene information and update background
        self.detect_and_update_scene(text)
    
    def detect_and_update_scene(self, text):
        """Detect current scene from game text and update background"""
        try:
            # Scene detection patterns
            scene_patterns = [
                ('Cave Entrance', ['cave entrance', 'rocky entrance', 'mouth of the cave']),
                ('Skull Chamber', ['skull chamber', 'chamber of skulls', 'ominous chamber']),
                ('Primitive Village', ['primitive village', 'village', 'huts', 'cave people']),
                ('Alley', ['alley', 'dark alley', 'narrow alley']),
                ('Armory', ['armory', 'weapon shop', 'weapons']),
                ('Cave People Chief House', ['chief house', 'chief', 'leader'])
            ]
            
            text_lower = text.lower()
            
            for scene_name, keywords in scene_patterns:
                if any(keyword in text_lower for keyword in keywords):
                    self.update_scene_background(scene_name)
                    break
                    
        except Exception as e:
            print(f"Scene detection error: {e}")
    
    def create_demo_graphics_test(self):
        """Create a simple graphics test window"""
        try:
            test_window = tk.Toplevel(self.root)
            test_window.title("Graphics Test - SHABUYA Assets")
            test_window.geometry("600x500")
            test_window.configure(bg='#1a0f08')
            
            # Test sprites
            sprite_frame = tk.LabelFrame(test_window, text="Character Sprites", 
                                       fg='#DAA520', bg='#2c1810')
            sprite_frame.pack(pady=10, padx=10, fill=tk.X)
            
            sprite_row = tk.Frame(sprite_frame, bg='#2c1810')
            sprite_row.pack(pady=10)
            
            for name, sprite in self.character_sprites.items():
                col = tk.Frame(sprite_row, bg='#2c1810')
                col.pack(side=tk.LEFT, padx=10)
                
                tk.Label(col, image=sprite, bg='#2c1810').pack()
                tk.Label(col, text=name.title(), fg='#CD853F', 
                        bg='#2c1810').pack()
            
            # Test backgrounds
            bg_frame = tk.LabelFrame(test_window, text="Scene Backgrounds", 
                                   fg='#DAA520', bg='#2c1810')
            bg_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
            
            # Background display canvas
            bg_canvas = tk.Canvas(bg_frame, width=400, height=300, 
                                bg='#1a0f08', highlightthickness=0)
            bg_canvas.pack(pady=10)
            
            # Background selection buttons
            button_frame = tk.Frame(bg_frame, bg='#2c1810')
            button_frame.pack()
            
            def show_background(bg_name):
                if bg_name in self.background_images:
                    bg_canvas.delete("all")
                    bg_canvas.create_image(200, 150, 
                                         image=self.background_images[bg_name])
            
            for bg_name in self.background_images.keys():
                tk.Button(button_frame, text=bg_name.replace('_', ' ').title(),
                         command=lambda name=bg_name: show_background(name),
                         bg='#8B4513', fg='white', font=("Arial", 9)).pack(
                         side=tk.LEFT, padx=5)
            
            # Show first background by default
            if self.background_images:
                first_bg = list(self.background_images.keys())[0]
                show_background(first_bg)
            
        except Exception as e:
            print(f"Graphics test error: {e}")
    

def main():
    """Main entry point for enhanced GUI"""
    try:
        print("🎮 Starting SHABUYA Enhanced GUI...")
        
        # Check for required dependencies
        missing_deps = []
        try:
            import PIL
        except ImportError:
            missing_deps.append("Pillow")
        
        if missing_deps:
            print(f"⚠️ Missing dependencies: {', '.join(missing_deps)}")
            print("Install with: pip install " + " ".join(missing_deps))
            print("Falling back to basic GUI...")
            
            # Fallback to basic GUI
            from gui import main as basic_gui_main
            basic_gui_main()
            return
        
        # Launch enhanced GUI
        app = EnhancedGameGUI()
        app.run()
        
    except Exception as e:
        print(f"❌ Enhanced GUI failed to start: {e}")
        messagebox.showerror("Error", f"Failed to start enhanced GUI: {e}")
        
        # Try fallback to basic GUI
        try:
            from gui import main as basic_gui_main
            print("🔄 Falling back to basic GUI...")
            basic_gui_main()
        except Exception as fallback_error:
            print(f"❌ Fallback GUI also failed: {fallback_error}")
            sys.exit(1)

if __name__ == "__main__":
    main()
